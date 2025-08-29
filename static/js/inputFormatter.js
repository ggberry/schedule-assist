document.getElementById('class-input').addEventListener('keyup', function() {
    let value = this.value.replace(/-/g, '');
    let formattedValue = value.match(/.{1,3}/g);

    if (formattedValue) {
        this.value = formattedValue.join('-');
    } else {
        this.value = '';
    }
});



document.getElementById('class-input').addEventListener('paste', function() {
    event.preventDefault();

    const field = document.getElementById('class-input');
    field.value = "e";
});