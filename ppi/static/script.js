document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener("click", async (event) => {
            event.preventDefault();

            const buttonElement = event.currentTarget;
            const form = buttonElement.closest(".delete-form");

            if (!form) {
                console.error("Erro: Formulário não encontrado!");
                return;
            }

            const postId = form.getAttribute("data-id");
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
            const url = form.getAttribute("action");

            if (confirm("Tem certeza que deseja excluir este projeto?")) {
                try {
                    const response = await fetch(url, {
                        method: "POST",
                        headers: {
                            "X-CSRFToken": csrfToken,
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({})  
                    });

                    // ✅ Captura a resposta bruta antes de tentar converter para JSON
                    const rawText = await response.text();
                    console.log("Resposta bruta do servidor:", rawText);

                    // Tenta converter a resposta para JSON
                    let data;
                    try {
                        data = JSON.parse(rawText);
                    } catch (jsonError) {
                        throw new Error("A resposta não é um JSON válido: " + rawText);
                    }

                    // ✅ Agora verifica se o JSON contém os dados esperados
                    if (data.sucesso) {
                        alert("Projeto deletado com sucesso!");
                        document.getElementById(`projeto-${postId}`).remove();
                    } else {
                        alert(`Erro: ${data.erro || "Resposta inesperada do servidor"}`);
                    }
                } catch (error) {
                    console.error("Erro na requisição:", error);
                    alert("Erro na requisição: " + error.message);
                }
            }
        });
    });
});
