import json # Added for JSON parsing
import re
from langchain_core.messages import HumanMessage
from rich.console import Console
from rich.table import Table
from graph import graph

if __name__ == "__main__":
    console = Console()
    asset_input_str = "btc"

    initial_graph_input = {
        "messages": [HumanMessage(content=f"Analyze market sentiment and technicals for {asset_input_str}.")],
        "asset": asset_input_str
    }
    final_result = graph.invoke(initial_graph_input)

    if not (final_result["messages"] and len(final_result["messages"]) > 0):
        console.print("[bold red]Error: No messages in final_result.[/bold red]")
        exit()

    last_message_content_str = final_result["messages"][-1].content

    # Initialize default values for table
    asset_display = asset_input_str.upper()
    recommendation = "Error"
    confidence = "N/A"
    entry_price = "N/A"
    stop_loss = "N/A"
    take_profit_targets = "N/A"
    summary_details = "Error parsing agent output."

    try:
        # The content is expected to be a JSON string.
        # LLMs might wrap JSON in ```json ... ``` or just ``` ... ```.
        content_to_parse = last_message_content_str.strip()
        if content_to_parse.startswith("```json"):
            content_to_parse = content_to_parse[len("```json"):]
        elif content_to_parse.startswith("```"):
            content_to_parse = content_to_parse[len("```"):]

        if content_to_parse.endswith("```"):
            content_to_parse = content_to_parse[:-len("```")]

        data = json.loads(content_to_parse)

        asset_display = data.get("asset", asset_input_str.upper())
        recommendation = data.get("recommendation", "N/A")
        confidence = data.get("confidence", "N/A")
        entry_price_val = data.get("entry_price", "N/A")
        stop_loss_val = data.get("stop_loss", "N/A")
        take_profit_targets_list = data.get("take_profit_targets", ["N/A"])

        summary_details = data.get("summary", "No summary provided.")

        # Format for display
        entry_price = str(entry_price_val)
        stop_loss = str(stop_loss_val)
        take_profit_targets = ", ".join(map(str, take_profit_targets_list))

        # Combine details for the summary column for now
        summary_output = (
            f"Confidence: {confidence}\n"
            f"Entry: {entry_price}, SL: {stop_loss}, TP: {take_profit_targets}\n"
            f"--- Summary ---\n{summary_details}"
        )

    except json.JSONDecodeError:
        console.print(f"[bold red]Error: Could not decode JSON from agent output:[/bold red]\n{last_message_content_str}")
        summary_output = f"Error decoding JSON. Raw output:\n{last_message_content_str}"
        # Keep default error values for recommendation etc.
    except Exception as e:
        console.print(f"[bold red]Error processing agent output: {e}[/bold red]\n{last_message_content_str}")
        summary_output = f"Error processing output. Raw output:\n{last_message_content_str}"


    table = Table(title=f"Trading Recommendation for {asset_display}")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Details", style="green")

    table.add_row("Asset", asset_display)
    table.add_row("Recommendation", recommendation)
    table.add_row("Confidence", confidence)
    table.add_row("Entry Price", entry_price)
    table.add_row("Stop-Loss", stop_loss)
    table.add_row("Take Profit Targets", take_profit_targets)
    table.add_row("Strategy Summary", summary_details)

    console.print(table)

    # Optionally, print the raw JSON string for debugging
    # console.print("\n[bold]Raw JSON Output from Trading Strategist:[/bold]")
    # console.print(last_message_content_str)
