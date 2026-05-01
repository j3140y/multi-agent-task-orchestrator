
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o-mini"

def llm_call(prompt):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return resp.choices[0].message.content

def planner(task):
    return llm_call(f"将任务拆解为步骤:\n{task}")

def tool(step):
    if "搜索" in step:
        return f"[TOOL] 搜索完成: {step}"
    return None

def executor(step):
    tool_result = tool(step)
    return llm_call(f"执行步骤:{step}\n工具结果:{tool_result}")

def reviewer(task, results):
    return llm_call(f"任务:{task}\n结果:{results}\n是否完成?")

def run(task):
    print("=== PLAN ===")
    plan = planner(task)
    print(plan)

    steps = [s for s in plan.split("\n") if s.strip()]
    results = []

    print("\n=== EXECUTION ===")
    for s in steps:
        r = executor(s)
        print(s, "=>", r)
        results.append(r)

    print("\n=== REVIEW ===")
    review = reviewer(task, "\n".join(results))
    print(review)

if __name__ == "__main__":
    run("分析某产品用户增长下降原因并给出建议")
