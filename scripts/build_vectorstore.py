from pathlib import Path

import chromadb


ROOT = Path(__file__).resolve().parents[1]

KNOWLEDGE_BASE = (
    ROOT
    / "knowledge_base"
)

VECTORSTORE = (
    ROOT
    / "vectorstore"
    / "chroma"
)


COLLECTION_NAME = (
    "marketing_knowledge"
)


CHUNK_SIZE = 1800
CHUNK_OVERLAP = 300


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():

            chunks.append(
                chunk.strip()
            )

        start = (
            end - overlap
        )

        if start < 0:

            start = 0

    return chunks


def build_vectorstore():

    VECTORSTORE.mkdir(
        parents=True,
        exist_ok=True,
    )

    client = (
        chromadb.PersistentClient(
            path=str(VECTORSTORE)
        )
    )

    collection = (
        client.get_or_create_collection(
            name=COLLECTION_NAME
        )
    )

    documents = []

    ids = []

    metadatas = []

    for file_path in sorted(
        KNOWLEDGE_BASE.rglob("*.txt")
    ):

        text = file_path.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(text)

        relative_path = (
            file_path.relative_to(
                ROOT
            )
        )

        for index, chunk in enumerate(
            chunks
        ):

            documents.append(chunk)

            ids.append(
                f"{file_path.stem}-{index}"
            )

            metadatas.append(
                {
                    "source": str(
                        relative_path
                    ),
                    "category": file_path.parent.name,
                }
            )

    if documents:

        collection.upsert(
            documents=documents,
            ids=ids,
            metadatas=metadatas,
        )

    print(
        f"Indexed {len(documents)} chunks."
    )

    print(
        f"Vector store: {VECTORSTORE}"
    )


if __name__ == "__main__":

    build_vectorstore()