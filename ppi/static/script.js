
const pesquisarBtn = document.getElementById('pesquisar');

if (pesquisarBtn) {
    pesquisarBtn.addEventListener('click', () => {
        event.stopPropagation();
        pesquisarBtn.classList.toggle('mudarTamanho')
    });
    
    document.addEventListener('click', function() {
        pesquisarBtn.classList.remove('mudarTamanho');
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const deleteBtns = document.querySelectorAll('.delete-btn')

    deleteBtns.forEach(button => {
        button.addEventListener("click", (event) => {

            const buttonElement = event.target;
            const form = button.closest(".delete-form");

            if (!form) {
                console.error("Formulário não encontrado para o botão de exclusão.");
                return;
            }
            
            const postId = form.getAttribute("data-id");
            const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

            if (confirm("Tem certeza que deseja excluir este projeto?")) {
                fetch(`/projeto/excluir/${postId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrfToken,
                    },
                })
                        
                .then(response => response.json())

                .then(data => {
                    if (data["Sucesso!"]) {
                        alert("Projeto deletado com sucesso!");
                        form.closest(".card").remove();
                    } else {
                        alert(`Erro: ${data["Erro"]}`);
                    }
                })

                .catch(error => {
                    console.error(`Erro: ${data[Erro]}`);
                });
                
            }
        });
    });
});