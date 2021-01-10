import re

def check_infinite_loop(instructions):
    executed_steps = {}
    total_steps = len(instructions)
    accumulator = 0
    step = 0
    is_infinite_loop = False
    while step < total_steps:
        operation = instructions[step][0]
        argument = instructions[step][1]

        # print(f"Op = {operation}, arg = {argument}, step = {step}")    
        if step not in executed_steps:
            executed_steps[step] = 1
        else:
            is_infinite_loop = True
            # print( f"infinite loop detected ! back to step {step}.")
            break

        if operation == "acc":
            accumulator += argument
            step += 1
        elif operation == "jmp":
            step += argument
        else:
            step += 1
    return is_infinite_loop, accumulator


if __name__ == "__main__":
    stmts = []

    for stmt in [line.strip() for line in open("AdventOfCodeDay08.txt","r")]:
        st = re.findall(r"(\w+)\s+([+-]\d+)",stmt)
        operation = st[0][0]
        argument = int(st[0][1]) 
        stmts.append([operation,argument])


    for vstmt in {index: stmt for index, stmt in enumerate(stmts) if stmt[0] == "nop" or stmt[0] == "jmp"}:
        # swap instrunction between jmp and nop 
        stmts[vstmt][0] = "jmp" if  stmts[vstmt][0] == "nop" else "nop"
            
        is_infinite_loop, accumulator = check_infinite_loop(stmts)

        if is_infinite_loop:
            # revert back the instruction
            stmts[vstmt][0] = "jmp" if  stmts[vstmt][0] == "nop" else "nop"  
        else:
            print(f"changed step {vstmt} fixed infinite loop.")
            print(f"accumulator = {accumulator} ")
            #print(f"{stmts}")
            break
    
