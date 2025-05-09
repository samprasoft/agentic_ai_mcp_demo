import argparse

from langchain_mcp_connect import LangChainMcp

from app.streaming_agent import MCPDemo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Langchain Model Context Protocol demo"
    )
    parser.add_argument(
        "-q", "--query", type=str, help="Query to be executed", nargs="?"
    )
    args = parser.parse_args()

    mcp = LangChainMcp()
    tools = mcp.list_mcp_tools()
    agent = MCPDemo()

    if args.query:
        agent.start(tools, args.query)

    else:
        print("Welcome to MCP Demo! Type 'exit' or 'quit' to end the session.")
        print("Enter your query:")

        while True:
            try:
                query = input("> ").strip()
                if query.lower() in ["exit", "quit"]:
                    print("Goodbye!")
                    break
                if query:  # Only process non-empty queries
                    agent.start(tools, query)
                    print("\nEnter your next query:")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Enter your next query:")
