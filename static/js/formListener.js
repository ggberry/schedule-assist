function addFormListener(form, path) {
    form.addEventListener('submit',
        function(event) {
            event.preventDefault();
            const formData = new FormData(form);

            fetch(path, {
                method: 'POST',
                body: formData,
            }).then(() => {
                form.reset();
                window.location.reload();
            });
        }
    );
}

const classInputForm = document.getElementById("class-input-form");
const removeForms = document.querySelectorAll(".class-remove-form");

addFormListener(classInputForm, "/add-class");

removeForms.forEach(form => {
    addFormListener(form, "/remove-class");
});
