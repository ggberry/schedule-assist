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
            });
        }
    );
}

function addRemoveListener(form, path) {
    form.addEventListener('submit',
        function(event) {
            event.preventDefault();

            fetch(path, {
                method: 'POST',
                body: "HI!",
            })
        }
    );
}

const classInputForm = document.getElementById("class-input-form");
const classDisplayForm = document.getElementById("class-remove-form");

addFormListener(classInputForm, "/add-class");
addRemoveListener(classDisplayForm, "/remove-class");
