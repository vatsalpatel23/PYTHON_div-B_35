"""
PTMAE: Pure Python Transactional Micro-Banking & Audit Engine
=============================================================
A high-integrity transactional micro-banking and audit system built
strictly in pure Python 3.x with zero external dependencies.

HARD CONSTRAINTS ENFORCED:
- Imports: ONLY standard libraries 'random' and 'datetime'.
- Manual Parser: Zero use of str.split() or str.replace().
- Reductions: Zero use of max(), min(), sum() where loop tracking/reduction is required.
- Closures & Scope: Zero global variables used for state transfer or late binding.
- In-place Mutability: In-place queue cleaning without modifying object id() or re-binding.
- File Engine: In-place 'r+' mode record updating with chunk-wise shifting and f.truncate().
  Never rewrites entire file in 'w' mode.
- Resource Safety: All file descriptors safely managed via context managers or try-finally.
- OOP: Strictly uses super().__init__() without hardcoding base class names.
- Encapsulation: Strict name mangling for private balance and overdraft fields.
"""

# =====================================================================
# ALLOWED IMPORTS ONLY (Strictly 'random' and 'datetime')
# =====================================================================
import datetime
import random


# =====================================================================
# MODULE 1 — STATE ENGINE (Unit 1)
# =====================================================================

def calculate_compound_interest_and_penalty(
    principal,
    annual_rate,
    periods,
    compounding_frequency=1,
    penalty_rate=0.0,
    penalty_threshold=0.0
):

    
    """
    Computes compound interest and conditional penalties period-by-period
    using EXCLUSIVELY basic arithmetic operators: +, -, *, /, //, %, **.
    
    Zero math module functions and zero built-in min/max/sum are used.
    All accumulation and state progressions are tracked manually within the loop.
    
    Parameters:
        principal (float): Initial account balance or principal amount.
        annual_rate (float): Nominal annual interest rate (e.g., 0.06 for 6%).
        periods (int): Total number of simulation periods.
        compounding_frequency (int): Compounding cycles per period (default 1).
        penalty_rate (float): Penalty fraction applied if below threshold (e.g., 0.02).
        penalty_threshold (float): Balance threshold triggering penalty assessment.
        
    Returns:
        tuple: (final_balance, period_history)
            final_balance (float): Resulting balance after all periods.
            period_history (list): Log of dictionaries for each period's state.
    """


    current_balance = float(principal)
    period_history = []
    
    # Manual loop counter
    p = 0
    while p < periods:
        p = p + 1
        
        # Periodic rate and compounding factor using +, /, **
        rate_per_cycle = annual_rate / compounding_frequency
        compounding_factor = (1.0 + rate_per_cycle) ** compounding_frequency
        
        # New balance after compounding interest using * and -
        new_balance = current_balance * compounding_factor
        interest_earned = new_balance - current_balance
        current_balance = new_balance
        
        # Conditional penalty evaluation using comparison and * / -
        penalty_assessed = 0.0
        if current_balance < penalty_threshold:
            penalty_assessed = current_balance * penalty_rate
            current_balance = current_balance - penalty_assessed
            
        period_history.append({
            "period": p,
            "interest": interest_earned,
            "penalty": penalty_assessed,
            "balance": current_balance
        })
        
    return current_balance, period_history


def trajectory_guard(sequence, safety_threshold=100.0):


    """
    Evaluates an operational trajectory sequence and halts execution immediately
    upon detecting unsafe conditions using short-circuit logical operators ('and' / 'or').
    
    Condition for immediate halt:
        (balance < safety_threshold) OR (termination_flag is True)
    
    Parameters:
        sequence (iterable): Sequence of state steps (dicts, tuples, or objects).
        safety_threshold (float): Minimum permissible balance threshold.
        
    Returns:
        dict: Diagnostic summary containing execution status, halt reason,
              step count, and safe trajectory records.
    """


    safe_trajectory_log = []
    halted = False
    halt_reason = None
    step_index = 0
    
    for step in sequence:
        step_index = step_index + 1
        
        # Extract balance and termination flag from heterogeneous formats
        if isinstance(step, dict):
            balance = float(step.get("balance", 0.0))
            term_flag = step.get("terminate", False)
        elif isinstance(step, (list, tuple)):
            balance = float(step[1]) if len(step) > 1 else 0.0
            term_flag = step[2] if len(step) > 2 else False
        else:
            balance = float(getattr(step, "balance", 0.0))
            term_flag = getattr(step, "terminate", False)
            
        # Short-circuit logical evaluation:
        # If (balance < safety_threshold) evaluates to True, Python halts evaluation
        # of subsequent terms immediately, triggering the halt action.
        if (balance < safety_threshold) or (term_flag is True or term_flag == "TERMINATE"):
            halted = True
            halt_reason = (
                f"Balance {balance:.2f} fell below safety threshold of {safety_threshold:.2f}"
                if balance < safety_threshold
                else "Explicit termination flag encountered"
            )
            break
            
        safe_trajectory_log.append(step)
        
    return {
        "halted": halted,
        "halt_reason": halt_reason,
        "stopped_at_step": step_index if halted else None,
        "safe_steps_count": len(safe_trajectory_log),
        "safe_trajectory": safe_trajectory_log
    }


def run_cli_event_loop(account_registry=None, db_path="accounts.db"):
    """
    Interactive CLI event loop built strictly with NESTED while loops.
    
    Features:
    - Continues execution after both valid and invalid commands without crashing.
    - Exits ONLY on an explicit 'exit' command.
    - Outer loop governs system runtime state; inner loop governs session command dispatch.
    
    Parameters:
        account_registry (dict, optional): In-memory account objects registry.
        db_path (str): Path to persistent accounts database file.
    """
    if account_registry is None:
        account_registry = {}
        
    print("\n" + "=" * 65)
    print(" PTMAE: Pure Python Transactional Micro-Banking & Audit Engine")
    print("=" * 65)
    print("Type 'help' for available commands or 'exit' to terminate.\n")
    
    system_running = True
    
    # Outer while loop (System Runtime Level)
    while system_running:
        session_active = True
        
        # Inner while loop (Command Dispatch & Event Processing Level)
        while session_active:
            try:
                raw_input_line = input("PTMAE> ")
            except (EOFError, KeyboardInterrupt):
                print("\n[CLI] Session terminated by signal. Exiting.")
                session_active = False
                system_running = False
                break
                
            # Manual extraction of command tokens without str.split()
            cmd_tokens = parse_raw_log_line(raw_input_line, delimiter=" ")
            
            # Filter empty strings resulting from multiple spaces
            clean_tokens = []
            token_idx = 0
            while token_idx < len(cmd_tokens):
                tok = cmd_tokens[token_idx]
                if len(tok) > 0:
                    clean_tokens.append(tok)
                token_idx = token_idx + 1
                
            if len(clean_tokens) == 0:
                continue
                
            command = clean_tokens[0].lower()
            
            # 1. Exit command (The ONLY way to terminate the engine)
            if command == "exit":
                print("[CLI] Shutting down PTMAE engine safely. Goodbye.")
                session_active = False
                system_running = False
                break
                
            # 2. Help command
            elif command == "help":
                print("\nAvailable Commands:")
                print("  help                               Display this command menu")
                print("  list                               List all registered in-memory accounts")
                print("  create <id> <type> <balance>       Create an account (SAVINGS, CURRENT, CREDIT)")
                print("  deposit <id> <amount>              Deposit funds into an account")
                print("  withdraw <id> <amount>             Withdraw/settle funds from an account")
                print("  interest <p> <rate> <periods>      Simulate compound interest and penalties")
                print("  guard                              Run trajectory guard test sequence")
                print("  update <id> <type> <balance>       Update database record in-place via r+ mode")
                print("  audit                              Process and audit accounts database")
                print("  settle <amount>                    Run polymorphic batch settlement on all accounts")
                print("  exit                               Exit the application\n")
                
            # 3. List command
            elif command == "list":
                if len(account_registry) == 0:
                    print("[INFO] No in-memory accounts registered. Use 'create' command or run demonstration.")
                else:
                    print("\n--- In-Memory Accounts ---")
                    for aid, acc in account_registry.items():
                        print(f"  Account ID: {aid:<10} | Type: {type(acc).__name__:<16} | Balance: {acc.get_balance():.2f}")
                    print(f"Total Active Account Objects: {Account.total_accounts}\n")
                    
            # 4. Create command
            elif command == "create":
                if len(clean_tokens) < 4:
                    print("[ERROR] Usage: create <account_id> <SAVINGS|CURRENT|CREDIT> <balance>")
                    continue
                aid = clean_tokens[1]
                atype = clean_tokens[2].upper()
                try:
                    init_bal = float(clean_tokens[3])
                except ValueError:
                    print(f"[ERROR] Balance must be numeric. Received: '{clean_tokens[3]}'")
                    continue
                    
                if atype == "SAVINGS":
                    account_registry[aid] = SavingsAccount(aid, init_bal)
                elif atype == "CURRENT":
                    account_registry[aid] = CurrentAccount(aid, init_bal)
                elif atype == "CREDIT":
                    account_registry[aid] = CreditAccount(aid, init_bal)
                else:
                    print(f"[ERROR] Unknown account type: '{atype}'. Must be SAVINGS, CURRENT, or CREDIT.")
                    continue
                print(f"[SUCCESS] Created {atype} account '{aid}' with initial balance {init_bal:.2f}")
                
            # 5. Deposit command
            elif command == "deposit":
                if len(clean_tokens) < 3:
                    print("[ERROR] Usage: deposit <account_id> <amount>")
                    continue
                aid = clean_tokens[1]
                if aid not in account_registry:
                    print(f"[ERROR] Account '{aid}' not found in registry.")
                    continue
                try:
                    amt = float(clean_tokens[2])
                    if amt <= 0.0:
                        raise ValueError("Amount must be positive.")
                except ValueError as ve:
                    print(f"[ERROR] Invalid deposit amount: {ve}")
                    continue
                acc = account_registry[aid]
                acc.set_balance(acc.get_balance() + amt)
                print(f"[SUCCESS] Deposited {amt:.2f} into '{aid}'. New Balance: {acc.get_balance():.2f}")
                
            # 6. Withdraw / Settle command
            elif command == "withdraw":
                if len(clean_tokens) < 3:
                    print("[ERROR] Usage: withdraw <account_id> <amount>")
                    continue
                aid = clean_tokens[1]
                if aid not in account_registry:
                    print(f"[ERROR] Account '{aid}' not found in registry.")
                    continue
                try:
                    amt = float(clean_tokens[2])
                    if amt <= 0.0:
                        raise ValueError("Amount must be positive.")
                except ValueError as ve:
                    print(f"[ERROR] Invalid withdrawal amount: {ve}")
                    continue
                acc = account_registry[aid]
                try:
                    res = acc.process_settlement(amt)
                    print(f"[SUCCESS] Settlement completed for '{aid}'. New Balance: {res['new_balance']:.2f}")
                except BaseSystemError as bse:
                    print(f"[REJECTED] Settlement failed for '{aid}': {bse}")
                    
            # 7. Interest command
            elif command == "interest":
                if len(clean_tokens) < 4:
                    print("[ERROR] Usage: interest <principal> <annual_rate> <periods>")
                    continue
                try:
                    p_val = float(clean_tokens[1])
                    r_val = float(clean_tokens[2])
                    per_val = int(clean_tokens[3])
                except ValueError:
                    print("[ERROR] Principal, rate, and periods must be numeric.")
                    continue
                fin_bal, hist = calculate_compound_interest_and_penalty(
                    p_val, r_val, per_val, compounding_frequency=1, penalty_rate=0.02, penalty_threshold=500.0
                )
                print(f"[SIMULATION] Final Balance after {per_val} periods: {fin_bal:.2f}")
                print(f"             Total Interest/Penalty logs generated: {len(hist)}")
                
            # 8. Guard command
            elif command == "guard":
                test_seq = [
                    {"step": 1, "balance": 1200.0, "terminate": False},
                    {"step": 2, "balance": 450.0, "terminate": False},
                    {"step": 3, "balance": 80.0, "terminate": False}, # Falls below 100.0
                    {"step": 4, "balance": 2000.0, "terminate": False}
                ]
                guard_res = trajectory_guard(test_seq, safety_threshold=100.0)
                print(f"[GUARD] Result: Halted={guard_res['halted']} | Reason: {guard_res['halt_reason']}")
                print(f"        Processed {guard_res['safe_steps_count']} safe steps out of {len(test_seq)}.")
                
            # 9. Update command (in-place file engine)
            elif command == "update":
                if len(clean_tokens) < 4:
                    print("[ERROR] Usage: update <account_id> <type> <balance>")
                    continue
                aid = clean_tokens[1]
                atype = clean_tokens[2].upper()
                try:
                    bal = float(clean_tokens[3])
                except ValueError:
                    print("[ERROR] Balance must be numeric.")
                    continue
                try:
                    update_account_record_inplace(db_path, aid, new_account_type=atype, new_balance=bal)
                    print(f"[SUCCESS] Database record for '{aid}' updated in-place via r+ mode.")
                except BaseSystemError as err:
                    print(f"[ERROR] Database update failed: {err}")
                except Exception as ex:
                    print(f"[ERROR] File error: {ex}")
                    
            # 10. Audit command
            elif command == "audit":
                print("[INFO] Starting accounts database audit...")
                process_and_audit_accounts_file(db_path=db_path)
                
            # 11. Settle command (Batch polymorphic settlement)
            elif command == "settle":
                if len(clean_tokens) < 2:
                    print("[ERROR] Usage: settle <amount>")
                    continue
                try:
                    settle_amt = float(clean_tokens[1])
                except ValueError:
                    print("[ERROR] Settle amount must be numeric.")
                    continue
                acc_list = list(account_registry.values())
                if len(acc_list) == 0:
                    print("[INFO] No in-memory accounts to settle. Create some first.")
                    continue
                report = execute_batch_settlement(acc_list, settle_amt)
                print(f"[BATCH REPORT] Successes: {report['success_count']} | Failures: {report['failure_count']}")
                
            # Unknown / Invalid command (Continues loop safely)
            else:
                print(f"[ERROR] Unknown command: '{clean_tokens[0]}'. Type 'help' for command list.")


# =====================================================================
# MODULE 2 — LOG PARSER & CLOSURES (Unit 2)
# =====================================================================

def parse_raw_log_line(line, delimiter=",", quote_char='"'):
    """
    Parses a raw delimited string into clean string tokens MANUALLY.
    
    STRICT CONSTRAINTS SATISFIED:
    - Zero use of str.split() or str.replace().
    - Zero use of the csv module or regular expressions.
    - Uses explicit index tracking, character iteration, slicing, and state flags.
    - Correctly handles delimiters inside quoted fields as literal data.
    - Handles escaped quote pairs ("") inside quoted fields as a single literal quote.
    - Accurately captures empty fields and trailing delimiters.
    
    Parameters:
        line (str): Input log string line.
        delimiter (str): Field separator (default ',').
        quote_char (str): Quoting character (default '"').
        
    Returns:
        list: List of parsed string tokens.
    """
    # Strip trailing newline characters manually using slicing
    if len(line) > 0 and line[-1] == "\n":
        line = line[:-1]
    if len(line) > 0 and line[-1] == "\r":
        line = line[:-1]
        
    if len(line) == 0:
        return []
        
    tokens = []
    current_token_chars = []
    in_quotes = False
    i = 0
    n = len(line)
    
    while i < n:
        char = line[i]
        
        if in_quotes:
            if char == quote_char:
                # Check for escaped quote pair ("")
                if i + 1 < n and line[i + 1] == quote_char:
                    current_token_chars.append(quote_char)
                    i = i + 2
                    continue
                else:
                    # Closing quote
                    in_quotes = False
                    i = i + 1
                    continue
            else:
                current_token_chars.append(char)
                i = i + 1
                continue
        else:
            if char == quote_char:
                # Opening quote
                in_quotes = True
                i = i + 1
                continue
            elif char == delimiter:
                # Field boundary reached
                tokens.append("".join(current_token_chars))
                current_token_chars = []
                i = i + 1
                continue
            else:
                current_token_chars.append(char)
                i = i + 1
                continue
                
    # Append final token after loop terminates
    tokens.append("".join(current_token_chars))
    return tokens


def create_audit_filter(threshold):


    """
    Factory creating a stateful audit filter closure.
    
    CONSTRAINTS SATISFIED:
    - Returns a nested function using the 'nonlocal' keyword to maintain
      an independent count of audited records across successive invocations.
    - Zero global variables used.
    - Each filter instance maintains completely isolated state.
    
    Parameters:
        threshold (float): Minimum financial value triggering audit qualification.
        
    Returns:
        function: Filter closure accepting a record and returning boolean qualification.
    """


    audit_count = 0
    passed_count = 0
    
    def audit_filter(record):
        nonlocal audit_count, passed_count
        audit_count = audit_count + 1
        
        # Extract numerical value from record
        val = 0.0
        if isinstance(record, (int, float)):
            val = float(record)
        elif isinstance(record, dict):
            val = float(record.get("balance", record.get("amount", 0.0)))
        elif isinstance(record, (list, tuple)) and len(record) >= 3:
            try:
                val = float(record[2])
            except (ValueError, TypeError):
                val = 0.0
        elif hasattr(record, "get_balance"):
            val = float(record.get_balance())
            
        meets_criteria = (val >= threshold)
        if meets_criteria:
            passed_count = passed_count + 1
            
        return meets_criteria

    def get_audit_stats():


        """Returns the internal state of this specific filter closure."""


        nonlocal audit_count, passed_count
        return {
            "total_audited": audit_count,
            "total_passed": passed_count,
            "threshold": threshold
        }
        
    audit_filter.get_stats = get_audit_stats
    return audit_filter


def build_positional_criteria_filters(criteria_callables):


    """
    Builds a list of lambda filters in a loop where each lambda tests the
    k-th positional criterion of a record.
    
    CONSTRAINTS SATISFIED:
    - Avoids Python closure late-binding by binding the loop index k as a
      default argument (k=k).
    - Zero global variables used.
    
    Parameters:
        criteria_callables (list): List of predicate functions for each position.
        
    Returns:
        list: List of lambda filters [lambda rec, k=k: ...]
    """


    filter_lambdas = []
    
    for k in range(len(criteria_callables)):
        # k=k binds current iteration value of k at definition time
        filter_lambdas.append(
            lambda record, k=k: criteria_callables[k](record[k]) if k < len(record) else False
        )
        
    return filter_lambdas


# =====================================================================
# MODULE 3 — DATA INVERSION & IN-PLACE PROCESSING (Unit 3)
# =====================================================================

def invert_bank_services(raw_db):


    """
    Transforms a branch-indexed bank service database into a service-indexed
    reverse index using a SINGLE dict comprehension pipeline.
    
    Format:
        Input:
            raw_db = {
                "BRANCH_01": [("Acc1@1", {"DEPOSIT", "UPI"}), ("Acc1@2", {"LOAN", "UPI"})],
                "BRANCH_02": [("Acc101", {"SAVINGS", "UPI"}), ("Acc103", {"CARD", "DEPOSIT"})]
            }
        Output:
            key = service tag,
            value = alphabetically sorted list of unique (Account_ID, Branch_ID) tuples.
            
    CONSTRAINTS SATISFIED:
    - Implemented strictly with a SINGLE dict comprehension.
    - Values are unique and sorted alphabetically.
    
    Parameters:
        raw_db (dict): Branch-mapped accounts and service sets.
        
    Returns:
        dict: Inverted service catalog index.
    """


    return {
        service: sorted(list({
            (acc_id, branch_id)
            for branch_id, accounts in raw_db.items()
            for acc_id, services in accounts
            if service in services
        }))
        for service in sorted({
            s
            for accounts in raw_db.values()
            for _, services in accounts
            for s in services
        })
    }


def clean_transaction_queue(data_list):


    """
    Cleans a heterogeneous transaction queue IN-PLACE without creating a new list.
    
    STRICT CONSTRAINTS SATISFIED:
    - id(data_list) remains 100% unchanged before and after execution.
    - Zero re-binding of parameter (data_list = [...] is strictly forbidden).
    - Step 1: Converts every tuple element into a list.
    - Step 2: Removes even-numbered transaction IDs from every set via set difference.
    - Step 3: Sorts every embedded list descending.
    - Step 4: Removes duplicate primitive values by scanning the list and DELETING
              BY INDEX (del data_list[i]) with ZERO separate collections (no seen set/dict/list).
              
    Parameters:
        data_list (list): Heterogeneous transaction queue containing tuples,
                          lists, sets, numbers, and strings.
                          
    Returns:
        list: The exact same list object mutated in-place.
    """


    # Step 1: Convert every tuple element into a list
    idx = 0
    while idx < len(data_list):
        if isinstance(data_list[idx], tuple):
            data_list[idx] = list(data_list[idx])
        idx = idx + 1

    # Step 2: Remove even-numbered transaction IDs from every set via set difference
    idx = 0
    while idx < len(data_list):
        if isinstance(data_list[idx], set):
            evens = {elem for elem in data_list[idx] if isinstance(elem, int) and elem % 2 == 0}
            data_list[idx] = data_list[idx].difference(evens)
        idx = idx + 1

    # Step 3: Sort every embedded list descending
    idx = 0
    while idx < len(data_list):
        if isinstance(data_list[idx], list):
            try:
                data_list[idx].sort(reverse=True)
            except TypeError:
                # Heterogeneous fallback sorting using string representation
                data_list[idx].sort(key=lambda x: str(x), reverse=True)
        idx = idx + 1

    # Step 4: Remove duplicate primitive values by scanning and DELETING BY INDEX
    # Strictly zero separate collections (no set, no dict, no tracking list)
    i = 0
    while i < len(data_list):
        item = data_list[i]
        # Identify primitive types: int, float, str, bool
        if isinstance(item, (int, float, str, bool)) and item is not None:
            duplicate_found = False
            j = 0
            while j < i:
                prev_item = data_list[j]
                # Type identity check ensures True != 1 and False != 0
                if type(prev_item) is type(item) and prev_item == item:
                    duplicate_found = True
                    break
                j = j + 1
                
            if duplicate_found:
                del data_list[i]
                # Index shifts left, so do not increment i
                continue
                
        i = i + 1

    return data_list


# =====================================================================
# MODULE 4 — FILE ENGINE & LOGGING (Unit 4)
# =====================================================================

class BaseSystemError(Exception):
    """Root exception class for all PTMAE transactional engine errors."""
    pass


class CorruptedRecordError(BaseSystemError):
    """Raised when an account record in database contains invalid, unparseable, or corrupt data."""
    pass


class OutOfBoundsError(BaseSystemError):
    """Raised when an operational limit (e.g. overdraft ceiling or index boundary) is exceeded."""
    pass


class InsufficientBalanceError(BaseSystemError):
    """Raised when an account lacks sufficient balance to perform a settlement or satisfy minimums."""
    pass


def update_account_record_inplace(file_path, target_account_id, new_account_type=None, new_balance=None):

    """
    Updates a specific account record in accounts.db in 'r+' mode.
    
    STRICT CONSTRAINTS SATISFIED:
    - Opens strictly in 'r+' mode with 'with' statement.
    - NEVER reads the entire file into memory or rewrites with 'w' mode.
    - Locates records with f.tell() and f.seek().
    - If payload size is identical, overwrites in place directly.
    - If payload shrinks (delta < 0), overwrites and shifts file remainder
      backwards in fixed-size chunks, then calls f.truncate().
    - If payload expands (delta > 0), shifts file remainder forwards from EOF
      backwards in fixed-size chunks, then writes new record at exact byte position.
    - Zero damage to neighbouring or adjacent lines.
    
    Parameters:
        file_path (str): Path to accounts.db.
        target_account_id (str): Account ID to locate and update.
        new_account_type (str, optional): Updated account type.
        new_balance (float, optional): Updated account balance.
    """


    CHUNK_SIZE = 64
    
    with open(file_path, "r+", newline="\n", encoding="utf-8") as f:
        found = False
        target_offset = None
        target_line = None
        
        # Pass 1: Locate target record and record byte offsets
        f.seek(0)
        while True:
            offset = f.tell()
            line = f.readline()
            if not line:
                break
                
            tokens = parse_raw_log_line(line)
            if len(tokens) >= 1 and tokens[0] == target_account_id:
                found = True
                target_offset = offset
                target_line = line
                break
                
        if not found:
            raise OutOfBoundsError(f"Account '{target_account_id}' not found in database '{file_path}'.")
            
        old_tokens = parse_raw_log_line(target_line)
        curr_type = old_tokens[1] if len(old_tokens) > 1 else "SAVINGS"
        curr_bal_str = old_tokens[2] if len(old_tokens) > 2 else "0.00"
        
        final_type = new_account_type if new_account_type is not None else curr_type
        if new_balance is not None:
            final_bal_str = f"{new_balance:.2f}"
        else:
            final_bal_str = curr_bal_str
            
        new_line = f"{target_account_id},{final_type},{final_bal_str}\n"
        
        old_len = len(target_line)
        new_len = len(new_line)
        delta = new_len - old_len
        rest_start_offset = target_offset + old_len
        
        # Case A: Identical payload size (Direct byte overwrite)
        if delta == 0:
            f.seek(target_offset)
            f.write(new_line)
            f.flush()
            
        # Case B: Shrinking payload (delta < 0)
        elif delta < 0:
            # Overwrite updated line first
            f.seek(target_offset)
            f.write(new_line)
            
            # Shift remainder of file backwards in chunks
            read_pos = rest_start_offset
            write_pos = target_offset + new_len
            
            while True:
                f.seek(read_pos)
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break
                read_pos = f.tell()
                
                f.seek(write_pos)
                f.write(chunk)
                write_pos = f.tell()
                
            # Truncate discarded trailing bytes
            f.truncate(write_pos)
            f.flush()
            
        # Case C: Expanding payload (delta > 0)
        else:
            # Move from EOF backwards to avoid overwriting unread data
            f.seek(0, 2)
            file_end = f.tell()
            curr_read_end = file_end
            
            while curr_read_end > rest_start_offset:
                remaining_bytes = curr_read_end - rest_start_offset
                chunk_len = CHUNK_SIZE if remaining_bytes > CHUNK_SIZE else remaining_bytes
                chunk_start = curr_read_end - chunk_len
                
                f.seek(chunk_start)
                chunk = f.read(chunk_len)
                
                f.seek(chunk_start + delta)
                f.write(chunk)
                curr_read_end = chunk_start
                
            # Write new line in allocated expanded gap
            f.seek(target_offset)
            f.write(new_line)
            f.flush()


def process_and_audit_accounts_file(db_path="accounts.db", ledger_path="ledger.txt", corrupted_log_path="corrupted.log"):


    """
    Audits accounts.db record-by-record using try-except-else-finally per record.
    
    STRICT CONSTRAINTS SATISFIED:
    - Detects corrupted records: wrong field count (!= 3), unknown account type,
      or non-numeric balance.
    - Valid records appended to ledger.txt with datetime timestamp.
    - Corrupted records appended to corrupted.log WITH EXACT LINE NUMBER.
    - finally block on every run reports processed and rejected record counts.
    - Zero use of max(), min(), sum().
    
    Parameters:
        db_path (str): Database file path.
        ledger_path (str): Ledger audit file path.
        corrupted_log_path (str): Corrupted records log path.
        
    Returns:
        dict: Summary of audit run (processed_count, rejected_count).
    """
    
    total_processed = 0
    total_rejected = 0
    line_number = 0
    
    try:
        with open(db_path, "r", newline="\n", encoding="utf-8") as db_file:
            while True:
                line = db_file.readline()
                if not line:
                    break
                    
                line_number = line_number + 1
                
                # Per-record try-except-else-finally
                record_valid = False
                record_data = None
                corruption_err = None
                
                try:
                    tokens = parse_raw_log_line(line)
                    if len(tokens) != 3:
                        raise CorruptedRecordError(
                            f"Field count violation: Expected exactly 3 fields, found {len(tokens)}"
                        )
                    acc_id = tokens[0].strip()
                    acc_type = tokens[1].strip()
                    bal_str = tokens[2].strip()
                    
                    if acc_type not in ("SAVINGS", "CURRENT", "CREDIT"):
                        raise CorruptedRecordError(
                            f"Unknown account type '{acc_type}'. Must be SAVINGS, CURRENT, or CREDIT"
                        )
                        
                    try:
                        balance_val = float(bal_str)
                    except ValueError:
                        raise CorruptedRecordError(f"Non-numeric balance value: '{bal_str}'")
                        
                    record_data = (acc_id, acc_type, balance_val)
                    record_valid = True
                    
                except CorruptedRecordError as err:
                    corruption_err = err
                    total_rejected = total_rejected + 1
                    with open(corrupted_log_path, "a", newline="\n", encoding="utf-8") as clog:
                        clog.write(f"Line {line_number}: {line.strip()} | Error: {err}\n")
                        
                else:
                    total_processed = total_processed + 1
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(ledger_path, "a", newline="\n", encoding="utf-8") as led:
                        led.write(
                            f"[{timestamp}] AUDIT_OK | Account: {record_data[0]} | "
                            f"Type: {record_data[1]} | Balance: {record_data[2]:.2f}\n"
                        )
                        
                finally:
                    # Per-record audit trail confirmation
                    pass
                    
    finally:
        # Mandatory finally block reporting counts on every run
        print(f"\n[AUDIT RUN SUMMARY]")
        print(f"  Processed Valid Records : {total_processed}")
        print(f"  Rejected Corrupt Records: {total_rejected}")
        print(f"  Total Lines Evaluated   : {line_number}")
        
    return {
        "processed_count": total_processed,
        "rejected_count": total_rejected,
        "total_lines": line_number
    }


# =====================================================================
# MODULE 5 — OOP & POLYMORPHISM (Unit 5)
# =====================================================================

class Account:
    """
    Abstract Base Account class providing foundational banking behaviors.
    
    STRICT CONSTRAINTS SATISFIED:
    - Encapsulation: private __balance, protected _account_id.
    - Class attribute total_accounts incremented upon instantiation.
    - Public getters and setters validating types and bounds.
    - Demonstrates Python name mangling (_Account__balance).
    """
    total_accounts = 0
    
    def __init__(self, account_id, initial_balance=0.0):
        """
        Initializes an Account instance.
        
        Parameters:
            account_id (str): Unique account identifier.
            initial_balance (float): Initial opening balance.
        """
        Account.total_accounts = Account.total_accounts + 1
        self._account_id = str(account_id)
        
        # Validate balance type and assign to private attribute
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a numeric value (int or float).")
        self.__balance = float(initial_balance)
        
    def get_account_id(self):
        """Returns the protected account identifier."""
        return self._account_id
        
    def get_balance(self):
        """Public getter for private __balance."""
        return self.__balance
        
    def set_balance(self, new_balance):
        """
        Public setter for private __balance with strict validation.
        
        Parameters:
            new_balance (float): Updated balance value.
        """
        if not isinstance(new_balance, (int, float)):
            raise TypeError("Balance must be a numeric value (int or float).")
        self.__balance = float(new_balance)
        
    def process_settlement(self, amount):
        """
        Polymorphic base settlement method. Subclasses override this method
        to apply specialized business constraints.
        """
        raise NotImplementedError("Subclasses must implement process_settlement().")


class SavingsAccount(Account):
    """
    Savings Account with minimum balance enforcement.
    
    CONSTRAINTS SATISFIED:
    - Inherits from Account and calls super().__init__() without hardcoded base name.
    - Rejects settlement if remaining balance would fall below 1000.00
      (raises InsufficientBalanceError).
    """
    MINIMUM_BALANCE = 1000.00
    
    def __init__(self, account_id, initial_balance=0.0):
        super().__init__(account_id, initial_balance)
        
    def process_settlement(self, amount):
        """
        Deducts settlement amount if remaining balance satisfies minimum threshold.
        """
        if not isinstance(amount, (int, float)) or amount <= 0.0:
            raise TypeError("Settlement amount must be a positive numeric value.")
            
        current = self.get_balance()
        projected = current - amount
        
        if projected < self.MINIMUM_BALANCE:
            raise InsufficientBalanceError(
                f"Settlement rejected for SavingsAccount '{self._account_id}': "
                f"Remaining balance {projected:.2f} falls below required minimum of {self.MINIMUM_BALANCE:.2f}"
            )
            
        self.set_balance(projected)
        return {
            "account_id": self._account_id,
            "type": "SAVINGS",
            "settled_amount": amount,
            "new_balance": self.get_balance()
        }


class CurrentAccount(Account):
    """
    Current Account supporting overdraft facilities up to a private limit.
    
    CONSTRAINTS SATISFIED:
    - Inherits from Account and calls super().__init__() without hardcoded base name.
    - Encapsulates private __overdraft_limit with getter/setter.
    - Allows balance to go negative down to -__overdraft_limit.
    - Raises OutOfBoundsError if settlement exceeds overdraft ceiling.
    """
    def __init__(self, account_id, initial_balance=0.0, overdraft_limit=5000.00):
        super().__init__(account_id, initial_balance)
        if not isinstance(overdraft_limit, (int, float)) or overdraft_limit < 0.0:
            raise TypeError("Overdraft limit must be a non-negative numeric value.")
        self.__overdraft_limit = float(overdraft_limit)
        
    def get_overdraft_limit(self):
        """Getter for private __overdraft_limit."""
        return self.__overdraft_limit
        
    def set_overdraft_limit(self, limit):
        """Setter for private __overdraft_limit."""
        if not isinstance(limit, (int, float)) or limit < 0.0:
            raise TypeError("Overdraft limit must be a non-negative numeric value.")
        self.__overdraft_limit = float(limit)
        
    def process_settlement(self, amount):
        """
        Deducts settlement amount permitting overdraft up to private limit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0.0:
            raise TypeError("Settlement amount must be a positive numeric value.")
            
        current = self.get_balance()
        projected = current - amount
        
        if projected < -self.__overdraft_limit:
            raise OutOfBoundsError(
                f"Settlement rejected for CurrentAccount '{self._account_id}': "
                f"Projected balance {projected:.2f} exceeds overdraft limit of {self.__overdraft_limit:.2f}"
            )
            
        self.set_balance(projected)
        return {
            "account_id": self._account_id,
            "type": "CURRENT",
            "settled_amount": amount,
            "new_balance": self.get_balance()
        }


class CreditAccount(Account):
    """
    Credit Account applying a surcharge and deducting from available credit limit.
    
    CONSTRAINTS SATISFIED:
    - Inherits from Account and calls super().__init__() without hardcoded base name.
    - Adds a mandatory 2.5% surcharge to settlement amount before deducting.
    - Raises InsufficientBalanceError if total charge exceeds available credit limit.
    """
    SURCHARGE_RATE = 0.025 # 2.5% surcharge
    
    def __init__(self, account_id, credit_limit=10000.00):
        super().__init__(account_id, credit_limit)
        
    def process_settlement(self, amount):
        """
        Adds 2.5% surcharge to amount and deducts from available credit limit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0.0:
            raise TypeError("Settlement amount must be a positive numeric value.")
            
        surcharge = amount * self.SURCHARGE_RATE
        total_deduction = amount + surcharge
        current = self.get_balance()
        projected = current - total_deduction
        
        if projected < 0.0:
            raise InsufficientBalanceError(
                f"Settlement rejected for CreditAccount '{self._account_id}': "
                f"Total required deduction {total_deduction:.2f} (including 2.5% surcharge {surcharge:.2f}) "
                f"exceeds available credit limit of {current:.2f}"
            )
            
        self.set_balance(projected)
        return {
            "account_id": self._account_id,
            "type": "CREDIT",
            "base_amount": amount,
            "surcharge": surcharge,
            "total_deduction": total_deduction,
            "new_balance": self.get_balance()
        }


def execute_batch_settlement(account_list, transaction_amount):
    """
    Executes polymorphic settlements across a heterogeneous list of accounts.
    
    STRICT CONSTRAINTS SATISFIED:
    - Polymorphic dispatch: invokes acc.process_settlement() dynamically.
    - Isolation: EACH settlement call is wrapped in its own isolated try-except
      block so a failure on one account never aborts subsequent accounts.
    - Reductions: Zero use of max(), min(), sum() for loop tracking or totals.
    
    Parameters:
        account_list (list): Collection of Account subclass instances.
        transaction_amount (float): Settlement amount to apply.
        
    Returns:
        dict: Summary containing success_count, failure_count, success_logs,
              and failure_logs.
    """
    success_logs = []
    failure_logs = []
    success_count = 0
    failure_count = 0
    total_settled_volume = 0.0
    
    for acc in account_list:
        try:
            res = acc.process_settlement(transaction_amount)
            success_logs.append(res)
            success_count = success_count + 1
            total_settled_volume = total_settled_volume + transaction_amount
        except BaseSystemError as err:
            failure_logs.append({
                "account_id": acc.get_account_id(),
                "account_type": type(acc).__name__,
                "error": str(err)
            })
            failure_count = failure_count + 1
        except Exception as unexpected:
            failure_logs.append({
                "account_id": acc.get_account_id(),
                "account_type": type(acc).__name__,
                "error": f"Unexpected error: {unexpected}"
            })
            failure_count = failure_count + 1
            
    return {
        "success_count": success_count,
        "failure_count": failure_count,
        "total_settled_volume": total_settled_volume,
        "success_logs": success_logs,
        "failure_logs": failure_logs
    }


# =====================================================================
# VERIFICATION & DEMONSTRATION SUITE
# =====================================================================

def run_comprehensive_demonstration():
    """
    Runs an exhaustive demonstration exercising every functional requirement
    (FR-1.1 through FR-5.3) and verifying non-functional rules.
    """
    print("\n" + "=" * 75)
    print(" PTMAE: COMPREHENSIVE VERIFICATION & DEMONSTRATION SUITE")
    print("=" * 75)

    # -----------------------------------------------------------------
    # UNIT 1 DEMONSTRATION: State Engine
    # -----------------------------------------------------------------
    print("\n>>> [UNIT 1] State Engine: Compound Interest & Trajectory Guard")
    principal = 1000.0
    rate = 0.08
    periods = 5
    final_bal, hist = calculate_compound_interest_and_penalty(
        principal=principal,
        annual_rate=rate,
        periods=periods,
        compounding_frequency=4,
        penalty_rate=0.05,
        penalty_threshold=1200.0
    )
    print(f"  Compound Interest Simulation:")
    print(f"    Principal: {principal:.2f} | Annual Rate: {rate*100}% | Periods: {periods}")
    print(f"    Calculated Final Balance (arithmetic operators only): {final_bal:.2f}")
    print(f"    Generated History Steps: {len(hist)}")

    # Trajectory Guard with short-circuit evaluation
    sample_trajectory = [
        {"step": 1, "balance": 1500.0, "terminate": False},
        {"step": 2, "balance": 850.0, "terminate": False},
        {"step": 3, "balance": 45.0, "terminate": False}, # Falls below safety threshold 100.0
        {"step": 4, "balance": 2000.0, "terminate": False} # Must never be reached
    ]
    guard_output = trajectory_guard(sample_trajectory, safety_threshold=100.0)
    print(f"  Trajectory Guard Evaluation:")
    print(f"    Halt Triggered: {guard_output['halted']}")
    print(f"    Halt Reason   : {guard_output['halt_reason']}")
    print(f"    Stopped Step  : {guard_output['stopped_at_step']} (halted immediately via short-circuit)")

    # -----------------------------------------------------------------
    # UNIT 2 DEMONSTRATION: Log Parser & Closures
    # -----------------------------------------------------------------
    print("\n>>> [UNIT 2] Manual Log Parser & Stateful Closures")
    test_log_lines = [
        'Acc101,SAVINGS,"5,200.00",ACTIVE',
        'Acc102,"Current ""Special"" Account",15000.00',
        'Acc103,SAVINGS,,',
        'Acc104,"",0.00'
    ]
    print("  Manual Parser (no str.split, no str.replace, no csv):")
    for t_line in test_log_lines:
        tokens = parse_raw_log_line(t_line)
        print(f"    Raw: {t_line:<45} -> Tokens: {tokens}")

    # Stateful Audit Filter Closures
    print("  Stateful Audit Filter Closures (independent nonlocal counters):")
    filter_high = create_audit_filter(threshold=5000.0)
    filter_low = create_audit_filter(threshold=1000.0)

    records_sample = [
        ("A1", "SAVINGS", 6000.0),
        ("A2", "CURRENT", 2500.0),
        ("A3", "SAVINGS", 800.0)
    ]
    for r in records_sample:
        filter_high(r)
        filter_low(r)

    print(f"    Filter High (Threshold 5000) Stats: {filter_high.get_stats()}")
    print(f"    Filter Low  (Threshold 1000) Stats: {filter_low.get_stats()}")

    # Positional Lambda Filters avoiding late binding
    print("  Positional Criteria Lambdas (k=k default argument late-binding fix):")
    criteria = [
        lambda x: x.startswith("Acc"),
        lambda x: x in ("SAVINGS", "CURRENT", "CREDIT"),
        lambda x: float(x) >= 2000.0
    ]
    pos_filters = build_positional_criteria_filters(criteria)
    test_rec = ["Acc999", "SAVINGS", "3500.00"]
    r0 = pos_filters[0](test_rec) # tests position 0
    r1 = pos_filters[1](test_rec) # tests position 1
    r2 = pos_filters[2](test_rec) # tests position 2
    print(f"    Test Record: {test_rec}")
    print(f"    Position 0 (Account ID format) : {r0}")
    print(f"    Position 1 (Valid Type)        : {r1}")
    print(f"    Position 2 (Balance threshold) : {r2}")

    # -----------------------------------------------------------------
    # UNIT 3 DEMONSTRATION: Data Inversion & In-Place Processing
    # -----------------------------------------------------------------
    print("\n>>> [UNIT 3] Data Inversion & In-Place Processing")
    raw_db = {
        "BRANCH_01": [("Acc1@1", {"DEPOSIT", "UPI"}), ("Acc1@2", {"LOAN", "UPI"})],
        "BRANCH_02": [("Acc101", {"SAVINGS", "UPI"}), ("Acc103", {"CARD", "DEPOSIT"})]
    }
    inverted = invert_bank_services(raw_db)
    print("  Single Dict Comprehension Service Inversion:")
    for s_tag, acc_pairs in inverted.items():
        print(f"    {s_tag:<10}: {acc_pairs}")

    # In-place queue cleaning
    raw_queue = [101, (3, 1, 2), {2, 4, 5, 7}, [10, 50, 20], 101, "TXN_A", 42, "TXN_A", 101]
    original_queue_id = id(raw_queue)
    print("\n  In-Place Transaction Queue Cleaning:")
    print(f"    Before Cleaning: {raw_queue}")
    clean_transaction_queue(raw_queue)
    print(f"    After Cleaning : {raw_queue}")
    print(f"    id(data_list) Unchanged: {id(raw_queue) == original_queue_id} (id={original_queue_id})")

    # -----------------------------------------------------------------
    # UNIT 4 DEMONSTRATION: File Engine & Logging
    # -----------------------------------------------------------------
    print("\n>>> [UNIT 4] File Engine: In-Place r+ Shifting & Database Auditing")
    db_file_path = "accounts.db"
    ledger_file_path = "ledger.txt"
    corrupted_file_path = "corrupted.log"

    # Setup database file with known records (including intentional corruption for audit test)
    with open(db_file_path, "w", newline="\n", encoding="utf-8") as f:
        f.write("Acc101,SAVINGS,5200.00\n")
        f.write("Acc102,CURRENT,15000.00\n")
        f.write("Acc103,CREDIT,3500.50\n")
        f.write("AccCORRUPT1,UNKNOWN_TYPE,1000.00\n")
        f.write("AccCORRUPT2,SAVINGS,INVALID_BALANCE\n")
        f.write("AccCORRUPT3,ONLY_TWO_FIELDS\n")
        f.write("Acc104,SAVINGS,9200.00\n")

    # Reset ledger and corrupted log
    with open(ledger_file_path, "w", newline="\n", encoding="utf-8") as f:
        f.write("")
    with open(corrupted_file_path, "w", newline="\n", encoding="utf-8") as f:
        f.write("")

    print("  Initial Database Content:")
    with open(db_file_path, "r", newline="\n", encoding="utf-8") as f:
        for l in f:
            print(f"    {l.strip()}")

    # Test in-place update with expansion and contraction
    print("\n  Testing in-place r+ update on 'Acc102' (Contracting payload to 99.00):")
    update_account_record_inplace(db_file_path, "Acc102", new_balance=99.00)
    with open(db_file_path, "r", newline="\n", encoding="utf-8") as f:
        for l in f:
            print(f"    {l.strip()}")

    print("\n  Testing in-place r+ update on 'Acc102' (Expanding payload to 12345678.99):")
    update_account_record_inplace(db_file_path, "Acc102", new_balance=12345678.99)
    with open(db_file_path, "r", newline="\n", encoding="utf-8") as f:
        for l in f:
            print(f"    {l.strip()}")

    # Audit the accounts database
    print("\n  Executing process_and_audit_accounts_file():")
    audit_summary = process_and_audit_accounts_file(
        db_path=db_file_path,
        ledger_path=ledger_file_path,
        corrupted_log_path=corrupted_file_path
    )

    print(f"\n  Logged Corrupted Records (corrupted.log):")
    with open(corrupted_file_path, "r", newline="\n", encoding="utf-8") as f:
        for cl in f:
            print(f"    {cl.strip()}")

    # -----------------------------------------------------------------
    # UNIT 5 DEMONSTRATION: OOP & Polymorphic Batch Settlement
    # -----------------------------------------------------------------
    print("\n>>> [UNIT 5] OOP & Polymorphism: Subclasses & Batch Settlement")
    acc_sav = SavingsAccount("SAV_01", 3000.00)
    acc_curr = CurrentAccount("CURR_01", 2000.00, overdraft_limit=4000.00)
    acc_cred = CreditAccount("CRED_01", 5000.00)

    # Name mangling demonstration
    print("  Demonstration of Python Encapsulation & Name Mangling:")
    print(f"    Mangled attribute access (acc_sav._Account__balance) : {acc_sav._Account__balance:.2f} (SUCCESS)")
    try:
        val = acc_sav.__balance
    except AttributeError:
        print("    Direct private access (acc_sav.__balance)           : AttributeError (BLOCKED AS EXPECTED)")

    print(f"    Total Accounts Created Across System: {Account.total_accounts}")

    # Polymorphic batch settlement
    mixed_accounts = [
        SavingsAccount("SA_101", 2500.00), # 2500 - 1800 = 700 (< 1000 min) -> REJECTED
        CurrentAccount("CA_201", 500.00, overdraft_limit=2000.00), # 500 - 1800 = -1300 (> -2000) -> SUCCESS
        CreditAccount("CR_301", 3000.00),  # 1800 + 45 (2.5%) = 1845 (< 3000) -> SUCCESS
        SavingsAccount("SA_102", 5000.00)  # 5000 - 1800 = 3200 (> 1000 min) -> SUCCESS
    ]

    print("\n  Executing execute_batch_settlement(amount=1800.00) across mixed account types:")
    batch_report = execute_batch_settlement(mixed_accounts, 1800.00)
    print(f"    Successful Settlements: {batch_report['success_count']}")
    for s_log in batch_report["success_logs"]:
        print(f"      [OK] Account: {s_log['account_id']} | Type: {s_log['type']} | New Balance: {s_log['new_balance']:.2f}")

    print(f"    Failed Settlements    : {batch_report['failure_count']}")
    for f_log in batch_report["failure_logs"]:
        print(f"      [REJECTED] Account: {f_log['account_id']} | Type: {f_log['account_type']} | Error: {f_log['error']}")

    print("\n" + "=" * 75)
    print(" ALL UNIT DEMONSTRATIONS COMPLETED SUCCESSFULLY")
    print("=" * 75 + "\n")


# =====================================================================
# ENTRY POINT
# =====================================================================
if __name__ == "__main__":
    # 1. Run all comprehensive automated unit tests and demonstrations
    run_comprehensive_demonstration()
    
    # 2. Launch the interactive CLI event loop
    # Pre-populate registry with sample accounts for immediate CLI testing
    active_registry = {
        "Acc101": SavingsAccount("Acc101", 5200.00),
        "Acc102": CurrentAccount("Acc102", 15000.00, overdraft_limit=5000.00),
        "Acc103": CreditAccount("Acc103", 3500.50)
    }
    
    print("[SYSTEM] Entering interactive CLI. (Type 'exit' to terminate, or press Ctrl+D)\n")
    try:
        run_cli_event_loop(account_registry=active_registry, db_path="accounts.db")
    except (EOFError, KeyboardInterrupt):
        print("\n[SYSTEM] Terminating PTMAE engine.")
