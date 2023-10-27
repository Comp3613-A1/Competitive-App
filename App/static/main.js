
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

async function getResultData(){
    const response = await fetch('/api/results');
    return response.json();
}
function loadResults(results){
    const table = document.querySelector('#addResultsForm');
    for(let result of results){
        table.innerHTML += `<tr>
            <td>${results.competitionID}</td>
            <td>${results.studentID}</td>
            <td>${results.position}</td>
            <td>${results.rank}</td>
        </tr>`;
    }
}

async function main1(){
    const results = await getResultData();
    loadResults(results);
}

main();
main1();
