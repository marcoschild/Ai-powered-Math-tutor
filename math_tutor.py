from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

def solve_math_problem(problem):
    try:
        expr = sp.sympify(problem)
        solution = sp.solve(expr)
        return str(solution)
    except Exception as e:
        return f"Error solving proble: {str(e)}"

@app.route('/solve', methods=['POST']) 
def solve():
    data = request.json
    problem = data.get("problem","")
    solution = solve_math_problem(problem)
    return jsonify({"problem": problem, "solution": solution})

if __name__ == '__main__':
    app.run(debug=True)