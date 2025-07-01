import os
import openai
from typing import List
import graphviz

class CodebaseAssistant:
    def __init__(self, code_dir: str, doc_path: str, openai_api_key: str):
        self.code_dir = code_dir
        self.doc_path = doc_path
        openai.api_key = openai_api_key
        self.codebase = self._load_codebase()
        self.documentation = self._load_documentation()

    def _load_codebase(self) -> str:
        code = []
        for root, _, files in os.walk(self.code_dir):
            for file in files:
                if file.endswith('.cpp') or file.endswith('.h'):
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        code.append(f"// File: {file}\n" + f.read())
        return "\n".join(code)

    def _load_documentation(self) -> str:
        with open(self.doc_path, 'r', encoding='utf-8') as f:
            return f.read()

    def _restructure_query(self, query: str) -> str:
        prompt = (
            "Restructure the following user query to be more precise and efficient for codebase search:\n"
            f"Query: {query}\n"
            "Restructured Query:"
        )
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=64,
            temperature=0.2
        )
        return response.choices[0].text.strip()

    def _generate_response(self, query: str) -> str:
        prompt = (
            "You are an expert AI assistant for a codebase. "
            "Given the following codebase and documentation, answer the user's query. "
            "If relevant, provide a flowchart in Graphviz DOT format and a detailed explanation.\n\n"
            "Documentation:\n"
            f"{self.documentation}\n\n"
            "Codebase:\n"
            f"{self.codebase[:4000]}\n\n"  # Truncate for token limits
            f"User Query: {query}\n"
            "Response:"
        )
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.3
        )
        return response.choices[0].text.strip()

    def _extract_flowchart(self, response: str) -> str:
        # Extract Graphviz DOT code from response if present
        start = response.find('```dot')
        end = response.find('```', start + 1)
        if start != -1 and end != -1:
            return response[start + 6:end].strip()
        return ""

    def generate_flowchart_image(self, dot_code: str, output_path: str):
        graph = graphviz.Source(dot_code)
        graph.render(output_path, format='png', cleanup=True)

    def answer_query(self, query: str, flowchart_img_path: str = "flowchart"):
        restructured_query = self._restructure_query(query)
        response = self._generate_response(restructured_query)
        dot_code = self._extract_flowchart(response)
        if dot_code:
            self.generate_flowchart_image(dot_code, flowchart_img_path)
            print(f"Flowchart image saved to {flowchart_img_path}.png")
        print("Response:\n", response)

#Example usage:
#assistant = CodebaseAssistant(
#     code_dir=r"D:\GitHub Projects\chat-model\cpp-codebase-lm\src",
#     doc_path=r"D:\GitHub Projects\chat-model\cpp-codebase-lm\docs\documentation.md",
#     openai_api_key here
# )
#assistant.answer_query("How does the login function work?")