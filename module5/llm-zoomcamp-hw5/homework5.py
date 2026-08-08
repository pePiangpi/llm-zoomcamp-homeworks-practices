import os
from dotenv import load_dotenv
load_dotenv()

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from starter import RAGBase, rag as starter_rag

import sqlite3
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult


class SQLiteSpanExporter(SpanExporter):

    def __init__(self, db_path="traces.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS spans (
                name TEXT,
                start_time INTEGER,
                end_time INTEGER,
                input_tokens INTEGER,
                output_tokens INTEGER,
                cost REAL
            )
        """)
        self.conn.commit()

    def export(self, spans):
        for span in spans:
            attrs = dict(span.attributes or {})
            self.conn.execute(
                "INSERT INTO spans VALUES (?, ?, ?, ?, ?, ?)",
                (
                    span.name,
                    span.start_time,
                    span.end_time,
                    attrs.get("input_tokens"),
                    attrs.get("output_tokens"),
                    attrs.get("cost"),
                ),
            )
        self.conn.commit()
        return SpanExportResult.SUCCESS

    def shutdown(self):
        self.conn.close()

    def force_flush(self):
        return True

# Setup OpenTelemetry
provider = TracerProvider()
# provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
provider.add_span_processor(SimpleSpanProcessor(SQLiteSpanExporter("traces.db")))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("llm-zoomcamp")

class RAGTraced(RAGBase):
    def rag(self, query):
        with tracer.start_as_current_span("rag") as span:
            return super().rag(query)
            
    def search(self, query):
        with tracer.start_as_current_span("search") as span:
            return super().search(query)
            
    def llm(self, prompt):
        with tracer.start_as_current_span("llm") as span:
            # Call the base llm method which returns the raw response object
            response = super().llm(prompt)
            
            # Read token usage from the response and set span attributes
            usage = response.usage
            span.set_attribute("input_tokens", usage.input_tokens)
            span.set_attribute("output_tokens", usage.output_tokens)
            
            return response
# Run it
if __name__ == "__main__":
    rag = RAGTraced(index=starter_rag.index, llm_client=starter_rag.llm_client)
    query = "How does the agentic loop keep calling the model until it stops?"
    
    print("--- Running Traced RAG Pipeline ---")
    answer = rag.rag(query)
    
    print("\n--- Final Answer ---")
    print(answer)