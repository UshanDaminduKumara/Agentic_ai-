from langchain_tavily import TavilySearch


def get_tools(enabled: bool):
    tools = [TavilySearch(max_results=2)] if enabled else []
    print("TOOLS RETURNED:", tools)
    return tools
