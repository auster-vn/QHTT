import pulp
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
import matplotlib.pyplot as plt
import numpy as np
from math import gcd
from functools import reduce

console = Console()


def lcm_for_list(lst):
    def lcm(a, b):
        return abs(a * b) // gcd(int(a), int(b))

    return reduce(lcm, [abs(x) for x in lst if x != 0], 1)


def input_problem():
    console.rule("[bold cyan]Nhập dữ liệu bài toán tuyến tính")

    num_vars = IntPrompt.ask("🔢 Nhập số biến")
    objective_type = Prompt.ask(
        "🎯 Nhập loại hàm mục tiêu", choices=["max", "min"], default="max"
    )

    console.print(
        "🧮 Nhập hệ số hàm mục tiêu (cách nhau bởi dấu cách)",
        style="bold green",
    )
    c = [float(x) for x in input(">> ").split()]

    var_types = []
    for i in range(num_vars):
        var_type = Prompt.ask(
            f"Biến x{i+1} có loại gì?",
            choices=[">=0", "<=0", "tự do"],
            default=">=0",
        )
        var_types.append(var_type)

    num_constraints = IntPrompt.ask("🔒 Nhập số ràng buộc")

    A, b, constraint_types = [], [], []
    for i in range(num_constraints):
        console.rule(f"[yellow]Ràng buộc {i+1}")
        console.print("Nhập hệ số ràng buộc:", style="green")
        A.append([float(x) for x in input(">> ").split()])
        constraint_types.append(
            Prompt.ask("Dấu ràng buộc", choices=["<=", ">=", "="])
        )
        b.append(float(Prompt.ask("Giá trị b")))

    return num_vars, objective_type, c, A, b, constraint_types, var_types


def solve_lp(num_vars, objective_type, c, A, b, constraint_types, var_types):
    problem = pulp.LpProblem(
        "Linear_Problem",
        pulp.LpMaximize if objective_type == "max" else pulp.LpMinimize,
    )
    real_vars = []
    transformed_vars = []

    for i in range(num_vars):
        vtype = var_types[i]
        if vtype == ">=0":
            var = pulp.LpVariable(f"x{i+1}", lowBound=0)
            real_vars.append(var)
            transformed_vars.append(var)
        elif vtype == "<=0":
            new_var = pulp.LpVariable(f"x{i+1}_neg", lowBound=0)
            real_vars.append(-new_var)
            transformed_vars.append(new_var)
        elif vtype == "tự do":
            x_pos = pulp.LpVariable(f"x{i+1}_pos", lowBound=0)
            x_neg = pulp.LpVariable(f"x{i+1}_neg", lowBound=0)
            real_vars.append(x_pos - x_neg)
            transformed_vars.append((x_pos, x_neg))

    # Hàm mục tiêu
    expr = 0
    for i, coef in enumerate(c):
        if isinstance(real_vars[i], tuple):
            expr += coef * (real_vars[i][0] - real_vars[i][1])
        else:
            expr += coef * real_vars[i]
    problem += expr

    # Ràng buộc
    for i in range(len(A)):
        expr = 0
        for j in range(num_vars):
            aij = A[i][j]
            if isinstance(real_vars[j], tuple):
                expr += aij * (real_vars[j][0] - real_vars[j][1])
            else:
                expr += aij * real_vars[j]
        if constraint_types[i] == "<=":
            problem += expr <= b[i]
        elif constraint_types[i] == ">=":
            problem += expr >= b[i]
        elif constraint_types[i] == "=":
            problem += expr == b[i]

    problem.solve()
    return problem, transformed_vars


def display_result(problem, variables, c, objective_type):
    status = pulp.LpStatus[problem.status]
    console.rule("[bold blue]Kết quả")

    if status == "Unbounded":
        console.print("[red]🔓 Bài toán không giới nội (Unbounded).")
        if objective_type == "max":
            if any(ci > 0 for ci in c):
                console.print("↗️ Giá trị tối ưu tiến tới dương vô cùng.")
            else:
                console.print("↘️ Giá trị tối ưu tiến tới âm vô cùng.")
        else:
            if any(ci < 0 for ci in c):
                console.print("↘️ Giá trị tối ưu tiến tới âm vô cùng.")
            else:
                console.print("↗️ Giá trị tối ưu tiến tới dương vô cùng.")
    elif status == "Infeasible":
        console.print("[red]❌ Bài toán vô nghiệm (Infeasible).")
    elif status == "Optimal":
        table = Table(title="📈 Giá trị tối ưu")
        table.add_column("Biến", justify="center", style="cyan")
        table.add_column("Giá trị", justify="center", style="green")

        for v in variables:
            if isinstance(v, tuple):
                table.add_row(v[0].name, f"{v[0].varValue:.2f}")
                table.add_row(v[1].name, f"{v[1].varValue:.2f}")
            else:
                table.add_row(v.name, f"{v.varValue:.2f}")

        console.print(table)
        console.print(
            f"[bold green]🎯 Giá trị tối ưu: {pulp.value(problem.objective):.2f}"
        )
    else:
        console.print(f"[red]Trạng thái không xác định: {status}")


def plot_2d_feasible_region(c, A, b, constraint_types):
    if len(c) != 2:
        console.print("[yellow]⚠️ Không thể vẽ hình học vì số biến khác 2.")
        return

    x = np.linspace(0, 10, 400)
    plt.figure(figsize=(8, 6))

    for i in range(len(A)):
        a1, a2 = A[i]
        bi = b[i]
        if a2 != 0:
            y = (bi - a1 * x) / a2
            plt.plot(x, y, label=f"Ràng buộc {i+1}")
            if constraint_types[i] == "<=":
                plt.fill_between(x, y, 10, where=(y <= 10), alpha=0.2)
            elif constraint_types[i] == ">=":
                plt.fill_between(x, y, 0, where=(y >= 0), alpha=0.2)
        else:
            x_val = bi / a1 if a1 != 0 else 0
            plt.axvline(x=x_val, label=f"Ràng buộc {i+1}")

    # Vẽ hàm mục tiêu
    z = lcm_for_list(c)
    if c[1] != 0:
        y = (z - c[0] * x) / c[1]
        plt.plot(x, y, "--", color="red", label=f"Hàm mục tiêu z={z}")

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Vùng nghiệm khả thi và hàm mục tiêu")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    console.print(
        Panel.fit(
            "[bold yellow]💡 GIẢI BÀI TOÁN QUY HOẠCH TUYẾN TÍNH",
            border_style="bold blue",
        )
    )
    num_vars, objective_type, c, A, b, constraint_types, var_types = (
        input_problem()
    )
    problem, variables = solve_lp(
        num_vars, objective_type, c, A, b, constraint_types, var_types
    )
    display_result(problem, variables, c, objective_type)
    plot_2d_feasible_region(c, A, b, constraint_types)


if __name__ == "__main__":
    main()
