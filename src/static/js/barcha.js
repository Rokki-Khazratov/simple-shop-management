
const name1 = document.querySelector('name1'),
    name2 = document.querySelector('name2'),
    name3 = document.querySelector('name3'),
    name4 = document.querySelector('name4'),
    tds = document.querySelector('td'),
    tbody = document.querySelector('tbody');

const tr = document.createElement('tr');
const td = document.createElement('td');
const td1 = document.createElement('td');
const td2 = document.createElement('td');
const td3 = document.createElement('td');
const td4 = document.createElement('td');
const td5 = document.createElement('td');
const td6 = document.createElement('td');

// const td1 = document.createElement('td');
// const td2 = document.createElement('td');
// const td3 = document.createElement('td');

tbody.append(tr)
tr.append(td, td1, td2, td3, td4, td5, td6)
