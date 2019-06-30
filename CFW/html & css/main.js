console.log('Hello');
const total = 200;

document.querySelector('textarea').addEventListener('input', function() {
    const length = document.querySelector('textarea').value.length;
    const remain = total - length;
    console.log(remain);
    document.getElementById('remainChar').innerText = remain;
})