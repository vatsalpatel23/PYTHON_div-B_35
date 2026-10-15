# PTMAE: Pure Python Transactional Micro-Banking & Audit Engine
**Technical Specification, Architectural Reference, and Compliance Report**

---

## 1. Executive Summary

The **Pure Python Transactional Micro-Banking & Audit Engine (PTMAE)** is an enterprise-grade transactional processing and audit system implemented strictly in **pure Python 3.x**. It operates under zero external third-party library dependencies and strictly enforces standard library restrictions, allowing **only** the `random` and `datetime` built-in modules.

PTMAE is designed to serve as an uncompromised demonstration of core computer science fundamentals, low-level data structure manipulation, manual state machines, pointer-like file I/O byte manipulation, closure scoping, and object-oriented polymorphism.

---

## 2. System Architecture & Class Diagrams

### 2.1 ASCII Architecture Flow Diagram

```
+=============================================================================+
|                      PTMAE SYSTEM ARCHITECTURE                              |
+=============================================================================+
|                                                                             |
|  [USER / CLI INTERFACE]                                                     |
|         │                                                                   |
|         ▼                                                                   |
|  +───────────────────────────────────────────────────────────────────────+  |
|  | MODULE 1: STATE ENGINE (Unit 1)                                       |  |
|  | - Nested while-loop event loop (Outer: Lifecycle / Inner: Dispatch)   |  |
|  | - Compound Interest & Penalty Engine (Operators: +, -, *, /, //, %, **)| |
|  | - Trajectory Guard (Short-Circuit: balance < threshold OR flag)       |  |
|  +──────────────────────────────────┬────────────────────────────────────+  |
|                                     │                                       |
|                                     ▼                                       |
|  +───────────────────────────────────────────────────────────────────────+  |
|  | MODULE 2: LOG PARSER & CLOSURES (Unit 2)                              |  |
|  | - Manual Lexer: Index tracking, character buffer, state flags        |  |
|  |   (Zero str.split, zero str.replace, handles quotes & delimiters)     |  |
|  | - Stateful Audit Filter: Enclosing closure with `nonlocal` counters    |  |
|  | - Positional Criteria Filters: Lambdas with `k=k` default binding     |  |
|  +──────────────────────────────────┬────────────────────────────────────+  |
|                                     │                                       |
|                                     ▼                                       |
|  +───────────────────────────────────────────────────────────────────────+  |
|  | MODULE 3: DATA INVERSION & IN-PLACE PROCESSING (Unit 3)               |  |
|  | - Service Catalog Inversion: Single Dict Comprehension Pipeline       |  |
|  | - Queue In-Place Cleaning: id(data_list) unchanged                    |  |
|  |   * Tuples -> Lists                                                   |  |
|  |   * Sets -> Difference update (remove even IDs)                       |  |
|  |   * Lists -> Descending sort                                          |  |
|  |   * Primitives -> Index deletion scan (No tracking collection)        |  |
|  +──────────────────────────────────┬────────────────────────────────────+  |
|                                     │                                       |
|         ┌───────────────────────────┴───────────────────────────┐           |
|         ▼                                                       ▼           |
|  +─────────────────────────────────────+ +───────────────────────────────+  |
|  | MODULE 4: FILE ENGINE (Unit 4)      | | MODULE 5: OOP & POLYMORPHISM  |  |
|  | - r+ In-Place Seek & Tell Updating  | | - Abstract Account Base Class |  |
|  | - Bidirectional Chunked Shifting    | |   (Private __balance, mangled)|  |
|  | - f.truncate() on payload shrink    | | - SavingsAccount (Min 1000)   |  |
|  | - Per-Record try-except-else-finally| | - CurrentAccount (Overdraft)  |  |
|  |   * Valid -> ledger.txt (timestamp) | | - CreditAccount (2.5% Surchg) |  |
|  |   * Invalid -> corrupted.log (line#)| | - Batch Settlement Dispatch   |  |
|  |   * Finally -> Run count reporting  | |   (Isolated try-except per acc|  |
|  |                                     | |    No max(), min(), sum())    |  |
|  +─────────────────────────────────────+ +───────────────────────────────+  |
|                                                                             |
+=============================================================================+
```

### 2.2 ASCII Class Hierarchy Diagram

```
                       +──────────────────────────+
                       |      Exception           |
                       +────────────┬─────────────+
                                    │
                                    ▼
                       +──────────────────────────+
                       |     BaseSystemError      |
                       +────────────┬─────────────+
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
+───────────────────────+ +───────────────────+ +────────────────────────────+
| CorruptedRecordError  | | OutOfBoundsError  | | InsufficientBalanceError   |
+───────────────────────+ +───────────────────+ +────────────────────────────+


                       +─────────────────────────────────────────+
                       |                Account                  |
                       +─────────────────────────────────────────+
                       | + total_accounts: int [Class Attr]      |
                       | # _account_id: str   [Protected]        |
                       | - __balance: float   [Private / Mangled]|
                       +─────────────────────────────────────────+
                       | + __init__(account_id, initial_balance) |
                       | + get_account_id() -> str               |
                       | + get_balance() -> float                |
                       | + set_balance(new_balance: float)       |
                       | + process_settlement(amount) [Abstract] |
                       +────────────────────┬────────────────────+
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        │                                   │                                   │
        ▼                                   ▼                                   ▼
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
|      SavingsAccount       | |      CurrentAccount       | |       CreditAccount       |
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
| + MINIMUM_BALANCE = 1000.0| | - __overdraft_limit: float| | + SURCHARGE_RATE = 0.025  |
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
| + __init__(id, bal)       | | + __init__(id, bal, limit)| | + __init__(id, limit)     |
|   calls super().__init__()| |   calls super().__init__()| |   calls super().__init__()|
| + process_settlement(amt) | | + get_overdraft_limit()   | | + process_settlement(amt) |
|   Rejects if proj < 1000  | | + set_overdraft_limit()   | |   Adds 2.5% surcharge,    |
|   raises InsufficientBal  | | + process_settlement(amt) | |   deducts from limit;     |
|                           | |   Allows neg to -limit;   | |   raises InsufficientBal  |
|                           | |   raises OutOfBoundsError | |                           |
+───────────────────────────+ +───────────────────────────+ +───────────────────────────+
```

---

## 3. State and Scope Tracking Table

The following table comprehensively documents variable scopes, mutation mechanisms, name mangling behaviors, and runtime isolation across PTMAE.

| Entity / Identifier | Originating Scope | Scope Modifier / Mechanism | Target Visibility | Purpose & Implementation Details |
| :--- | :--- | :--- | :--- | :--- |
| `Account.total_accounts` | Class Scope (`Account`) | Direct Class Attribute access (`Account.total_accounts`) | Public (Class & Instances) | Tracks aggregate instances spawned across entire application runtime; incremented in `Account.__init__()`. |
| `Account._account_id` | Instance Scope (`Account`) | Protected naming convention (`_`) | Derived Subclasses & Intrasystem | Preserves account identification without external re-assignment; accessible via `get_account_id()`. |
| `Account.__balance` | Instance Scope (`Account`) | Double-leading underscore private mangling (`_Account__balance`) | Class Internal Only | Encapsulates funds strictly. Direct access `acc.__balance` raises `AttributeError`. Access strictly channeled via `get_balance()` and `set_balance()`. |
| `CurrentAccount.__overdraft_limit` | Instance Scope (`CurrentAccount`) | Double-leading underscore private mangling (`_CurrentAccount__overdraft_limit`) | Subclass Internal Only | Restricts maximum credit overdraft threshold; exposed via dedicated getters/setters. |
| `audit_count` | Enclosing Scope (`create_audit_filter`) | `nonlocal audit_count` | Inner Closure (`audit_filter`) | Preserves continuous tally of records processed by that specific filter instance across multiple invocations without global state. |
| `passed_count` | Enclosing Scope (`create_audit_filter`) | `nonlocal passed_count` | Inner Closure (`audit_filter`) | Maintains count of records meeting or exceeding the financial threshold; state remains fully isolated per filter instance. |
| `k` (Positional Index) | Loop Local Scope (`build_positional_criteria_filters`) | Default argument binding (`k=k`) | Lambda Parameter Scope | Neutralizes Python's closure late-binding by binding current iteration index `k` at lambda definition time. |
| `system_running` | Function Scope (`run_cli_event_loop`) | Outer while loop flag | Outer Loop Only | Controls macro application lifecycle; exits only when explicit `"exit"` token is received. |
| `session_active` | Function Scope (`run_cli_event_loop`) | Inner while loop flag | Inner Loop Only | Controls command execution session; isolates sub-command failures so that invalid inputs never crash the engine. |
| `data_list` | Parameter Scope (`clean_transaction_queue`) | In-Place Mutation (`del`, `.sort()`, `[i] =`) | Caller Object Identity (`id()`) | Mutates caller list directly without re-binding (`data_list = [...]` forbidden). Guaranteed identical `id(data_list)`. |
| `total_processed` | Function Scope (`process_and_audit_accounts_file`) | Local counter (`+= 1`) | Enclosing function & `finally` | Accumulates valid audit lines without using `sum()`; reported in mandatory `finally` block on every run. |
| `total_rejected` | Function Scope (`process_and_audit_accounts_file`) | Local counter (`+= 1`) | Enclosing function & `finally` | Accumulates corrupted audit lines without using `sum()`; reported in mandatory `finally` block on every run. |

---

## 4. Module Compliance Checklist & Requirement Traceability

This matrix maps every functional requirement (FR) across Units 1 through 5 and non-functional requirements (NFRs) to their concrete implementation in `main.py`.

| ID | Module / Unit | Requirement Description | Compliance Status | Implementation Reference in `main.py` | Verification Evidence |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **FR-1.1** | Unit 1: State Engine | Interactive CLI event loop built with nested `while` loops; continues after valid/invalid commands; exits only on explicit `"exit"` | **MET** | Lines 142–330 (`run_cli_event_loop`) | Outer `while system_running` + inner `while session_active`. Handled `"exit"` cleanly in automated CLI test suite. |
| **FR-1.2** | Unit 1: State Engine | Compound interest & penalty calculation using ONLY `+ - * / // % **` inside loops (no math module) | **MET** | Lines 45–103 (`calculate_compound_interest_and_penalty`) | Zero `math` imports; compounding computed via `(1.0 + r/n)**n`; penalties subtracted via loop. |
| **FR-1.3** | Unit 1: State Engine | `trajectory_guard(sequence)` using short-circuit `and`/`or` evaluation to halt immediately when balance < threshold OR termination flag is found | **MET** | Lines 106–140 (`trajectory_guard`) | Short-circuit check `(balance < safety_threshold) or (term_flag is True ...)` halts step iteration immediately on breach. |
| **FR-2.1** | Unit 2: Parser & Closures | `parse_raw_log_line` manual token parser using index tracking, character iteration, slicing, and state flags (no `str.split`, no `str.replace`) | **MET** | Lines 337–421 (`parse_raw_log_line`) | Character-by-character while loop, state flag `in_quotes`, explicit slice slicing for newlines. Zero `.split(` or `.replace(`. |
| **FR-2.2** | Unit 2: Parser & Closures | Delimiter inside quoted field treated as data; escaped quote pair (`""`) inside quotes converted to single literal quote (`"`) | **MET** | Lines 380–405 (`parse_raw_log_line`) | Checks `char == quote_char` and `line[i+1] == quote_char`, advancing `i += 2` to yield literal `"`. |
| **FR-2.3** | Unit 2: Parser & Closures | Handle empty fields (e.g. `,,`) and trailing delimiters (e.g. `a,b,`) accurately | **MET** | Lines 410–420 (`parse_raw_log_line`) | Appends empty tokens upon successive delimiters and after loop completion. |
| **FR-2.4** | Unit 2: Parser & Closures | `create_audit_filter(threshold)` returning nested function using `nonlocal` to count audited records across calls independently | **MET** | Lines 424–478 (`create_audit_filter`) | Enclosed `audit_count` and `passed_count` modified with `nonlocal`. Tested independent isolation between filters. |
| **FR-2.5** | Unit 2: Parser & Closures | Build list of lambda filters in a loop where each lambda tests k-th positional criterion, avoiding late binding via `k=k` default argument | **MET** | Lines 481–508 (`build_positional_criteria_filters`) | Loop constructs `lambda record, k=k: ...`. Verified position 0, 1, 2 evaluated independently without late-binding corruption. |
| **FR-3.1** | Unit 3: Data Inversion | Produce service reverse index from `raw_db` using a SINGLE dict comprehension (key=service tag, value=sorted list of unique (Account, Branch) tuples) | **MET** | Lines 515–558 (`invert_bank_services`) | Single dict comprehension mapping `{service: sorted(list({(acc_id, branch_id) ...})) for service in sorted({...})}`. |
| **FR-3.2** | Unit 3: In-Place Processing | `clean_transaction_queue(data_list)` accepts heterogeneous list and modifies the SAME object in place (`id()` unchanged, no re-binding) | **MET** | Lines 561–636 (`clean_transaction_queue`) | `assert id(data_list) == initial_id` passes; zero parameter re-binding (`data_list = [...]` absent). |
| **FR-3.3** | Unit 3: In-Place Processing | Convert every tuple element into a list; remove even-numbered transaction IDs from every set via set difference | **MET** | Lines 585–602 (`clean_transaction_queue`) | `data_list[idx] = list(data_list[idx])` and `.difference(evens)` applied in place. |
| **FR-3.4** | Unit 3: In-Place Processing | Sort every embedded list descending; remove duplicate primitive values by scanning and DELETING BY INDEX (no separate collection for dedup) | **MET** | Lines 604–634 (`clean_transaction_queue`) | Embedded lists sorted via `.sort(reverse=True)`; duplicate primitives deleted with `del data_list[i]` with zero sets/dicts. |
| **FR-4.1** | Unit 4: File Engine | Exception hierarchy: `BaseSystemError(Exception)` with subclasses `CorruptedRecordError`, `OutOfBoundsError`, `InsufficientBalanceError` | **MET** | Lines 642–660 | Explicitly declared hierarchy with clear docstrings and error messaging. |
| **FR-4.2** | Unit 4: File Engine | Update `accounts.db` in `r+` mode: locate records with `f.tell()`/`f.seek()`, overwrite in place without damaging adjacent lines; chunked shifting & `f.truncate()` | **MET** | Lines 663–764 (`update_account_record_inplace`) | Strictly `"r+"` mode. Handles delta=0, delta<0 (shift backward + truncate), delta>0 (shift forward from EOF). Zero neighbouring line corruption. |
| **FR-4.3** | Unit 4: File Engine | Corrupted record identification: wrong field count (!= 3), non-numeric balance, or unknown account type | **MET** | Lines 790–825 (`process_and_audit_accounts_file`) | Checks token length == 3, membership in `("SAVINGS", "CURRENT", "CREDIT")`, and `float(bal_str)`. |
| **FR-4.4** | Unit 4: File Engine | Use `try-except-else-finally` per record. Valid updates -> `ledger.txt` (timestamp); invalid -> `corrupted.log` with line number; `finally` reports counts | **MET** | Lines 795–845 (`process_and_audit_accounts_file`) | Full `try-except-else-finally` structure. Timestamped ledger entries, line-numbered corruption logs, mandatory summary reporting. |
| **FR-5.1** | Unit 5: OOP & Polymorphism | `Account` class: private `__balance`, protected `_account_id`, class attribute `total_accounts`, getters/setters, name mangling demonstration | **MET** | Lines 860–920 (`Account`) | Mangled `_Account__balance` verified in test suite; `total_accounts` tracked; setters enforce numeric types. |
| **FR-5.2** | Unit 5: OOP & Polymorphism | Subclasses `SavingsAccount` (min 1000), `CurrentAccount` (overdraft limit), `CreditAccount` (2.5% surcharge); all calling `super().__init__()` | **MET** | Lines 923–1075 | All constructors invoke `super().__init__()` (no hardcoded base names); settlement business logic implemented. |
| **FR-5.3** | Unit 5: OOP & Polymorphism | `execute_batch_settlement` settles mixed list polymorphically; EACH call wrapped in isolated try-except; reports successes/failures (no min/max/sum) | **MET** | Lines 1078–1135 (`execute_batch_settlement`) | Isolated per-account try-except block; manual loop tallying (`success_count += 1`); zero use of `sum()`, `min()`, or `max()`. |
| **NFR-1** | Non-Functional | Strictly Python 3.x with ONLY `random` and `datetime` imports (no csv, json, re, math, os, sys, etc.) | **MET** | Lines 27–28 (`main.py`) | Grep verification confirms zero other imports exist in the file. |
| **NFR-2** | Non-Functional | Zero use of `str.split()` or `str.replace()` in the manual parser or command tokenization | **MET** | Lines 337–421, 187 | Zero `.split(` or `.replace(` calls across the entire codebase. |
| **NFR-3** | Non-Functional | Zero use of `max()`, `min()`, `sum()` where loop tracking or reductions are required | **MET** | Entire `main.py` | Verified zero invocations of `max()`, `min()`, or `sum()` anywhere in executable code. |
| **NFR-4** | Non-Functional | Every file opened with `with` statement or closed in a `finally` block | **MET** | Lines 190, 675, 765, 808, 818, etc. | 100% of file I/O operations managed within `with open(...)` context managers. |
| **NFR-5** | Non-Functional | Modular codebase with clear section labels and comprehensive docstrings on every class and function | **MET** | Entire `main.py` | All 5 modules clearly demarcated; docstrings specify parameters, returns, and algorithmic constraints. |

---

## 5. Algorithmic In-Depth Explanations

### 5.1 In-Place Chunked Shifting (`r+` Mode) in File Engine

The file engine updates records in `accounts.db` without reading the entire file into memory or recreating the file with `"w"` mode. 

Given an update on record $R$ at byte offset $O$:
1. **Delta Calculation**:
   $$\Delta = \text{len}(R_{\text{new}}) - \text{len}(R_{\text{old}})$$
2. **Case $\Delta = 0$ (Equal Size)**:
   The file pointer seeks directly to $O$ and overwrites $R_{\text{new}}$. Adjacent lines are untouched.
3. **Case $\Delta < 0$ (Payload Contraction)**:
   - $R_{\text{new}}$ is written at $O$.
   - The remaining file data starting at $O + \text{len}(R_{\text{old}})$ is shifted leftward by $|\Delta|$ bytes in fixed chunks of 64 bytes.
   - Because write position is always behind read position, no unread data is overwritten.
   - `f.truncate(new_eof)` is invoked to release trailing bytes.
4. **Case $\Delta > 0$ (Payload Expansion)**:
   - The remainder of the file is shifted rightward by $\Delta$ bytes starting from the end of the file (EOF) moving backward in 64-byte chunks toward $O + \text{len}(R_{\text{old}})$.
   - This backward pass guarantees that writing into expanded offsets never corrupts unread bytes.
   - $R_{\text{new}}$ is written into the gap at $O$.
   - All neighbouring records remain 100% byte-identical.

### 5.2 Manual Lexer State Machine

The manual lexer `parse_raw_log_line` implements a deterministic finite state machine (FSM):
- **States**: `OUTSIDE_QUOTES`, `INSIDE_QUOTES`.
- **Transitions**:
  - `OUTSIDE_QUOTES` + `quote_char` $\rightarrow$ Enter `INSIDE_QUOTES`.
  - `OUTSIDE_QUOTES` + `delimiter` $\rightarrow$ Emit accumulated token, reset buffer.
  - `INSIDE_QUOTES` + `quote_char`:
    - Lookahead `line[i+1] == quote_char` $\rightarrow$ Emit literal `quote_char`, advance index by 2 (handles `""`).
    - Otherwise $\rightarrow$ Return to `OUTSIDE_QUOTES`.
  - Delimiters encountered within `INSIDE_QUOTES` are appended directly to the token character buffer as data.
  - Slicing removes trailing `\r` and `\n` without calling `str.strip()` or `str.replace()`.

### 5.3 Deduplication by Index Deletion Without Tracking Sets

`clean_transaction_queue` performs in-place deduplication of primitive types without using tracking collections (`set()`, `dict()`, or `list()`):
- An outer pointer `i` traverses from $0$ to $\text{len}(\text{data\_list})$.
- For every primitive element at index `i`, an inner index `j` scans previous elements from $0$ to $i-1$.
- Strict type identity checks (`type(prev) is type(curr) and prev == curr`) distinguish between numeric equivalents (e.g. `1` vs `True`).
- If a match is found, `del data_list[i]` is invoked. Index `i` is not incremented, seamlessly evaluating the newly shifted element.

---

## 6. Execution and Verification Guide

### 6.1 Running the Automated Demonstration Suite

To execute the verification suite that exercises all 5 units:

```powershell
python main.py
```

When run, the engine executes:
1. **Unit 1**: Interest calculation without math library; trajectory guard short-circuit test.
2. **Unit 2**: Manual parsing of quoted/escaped logs; closure independent counters; positional lambda criteria.
3. **Unit 3**: Service catalog single-comprehension inversion; in-place queue cleaning with `id()` check.
4. **Unit 4**: `r+` in-place file update (shrink, expand, equal); corrupted file audit with `try-except-else-finally` and summary counts.
5. **Unit 5**: Name mangling demonstration; polymorphic settlement across savings, current, and credit accounts; batch execution.

### 6.2 Using the Interactive CLI

After the automated tests complete, the interactive CLI launches automatically. Available commands:
- `help`: Display command menu.
- `list`: View registered in-memory accounts.
- `create <id> <type> <balance>`: Spawn a new account (`SAVINGS`, `CURRENT`, or `CREDIT`).
- `deposit <id> <amount>`: Deposit funds.
- `withdraw <id> <amount>`: Perform settlement withdrawal.
- `interest <principal> <rate> <periods>`: Run interest and penalty simulation.
- `guard`: Test short-circuit trajectory guard.
- `update <id> <type> <balance>`: Execute in-place `r+` database update.
- `audit`: Run accounts database audit and logging.
- `settle <amount>`: Perform polymorphic batch settlement.
- `exit`: Safely shut down the PTMAE engine.
