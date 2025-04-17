from langchain_core.messages import HumanMessage
from graph import graph

if __name__ == "__main__":
    final_result = graph.invoke({"messages": [HumanMessage(content="btc")]})

    last_message = final_result["messages"]
    print(last_message)
