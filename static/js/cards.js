const firstCard = document.querySelectorAll('.first-char')
const cards = document.querySelectorAll('.char')
const hidden = document.querySelectorAll('.hidden')
const btnNext = document.getElementById('btn')
const examples = document.querySelector('.examples')

let num = `{{num}}`
let url = `/cards-data/${num}`

btnNext.onclick = function () {
    cards.forEach((e) => {
        // var e = e.cloneNode(true)
        let div = e.parentNode
        div.parentNode.classList.remove('border-danger')
        div.parentNode.classList.remove('border-success')
    })
    location.reload()
}

cardsData()

// fetch the data from the database and store it into the cards
function cardsData() {
    fetch(url)
        .then(response => response.json())
        .then(function (data) {
            console.log(data)

            if (num > 0 && data.length > 0) {
                hidden[0].classList.remove('hidden')
            }
            hidden[1].classList.add('hidden')

            firstCard[0].innerHTML = data[0]['character']
            firstCard[0].setAttribute("data-id", data[0]['id'])
            firstCard[1].innerHTML = (data[0]['kunyomi'].split(' '))[0] == 'n/a' ?
                (data[0]['onyomi'].split(' '))[0] :
                (data[0]['kunyomi'].split(' '))[0]


            let shuffleData = data.sort(function () {
                return Math.random() - 0.5
            })
            for (let card in cards) {
                cards[card].innerHTML = shuffleData[card]['meaning'].includes(',') ?
                    (shuffleData[card]['meaning'].split(','))[0] :
                    shuffleData[card]['meaning']

                cards[card].setAttribute('data-id', shuffleData[card]['id'])
            }

        })
}

// add event listener to all cards
cards.forEach((e) => {

    e.addEventListener('click', () => {

        let result = e.dataset.id == firstCard[0].dataset.id
        e.classList.remove('char')
        if (result) {
            let div = e.parentNode
            div.parentNode.classList.add('border-success')
        } else {
            let div = e.parentNode
            div.parentNode.classList.add('border-danger')
        }
        console.log(e)
        sendingData(result)
    })
})

// Sending POST request the database
function sendingData(result) {
    cards.forEach((e) => {
        if (e.dataset.id == firstCard[0].dataset.id) {
            let div = e.parentNode
            div.parentNode.classList.add('border-success')
        }
        e.removeEventListener('click', () => {

        })
    })

    console.log(result)
    let charId = firstCard[0].dataset.id
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'result': result, 'charId': charId })
    })
        .then(() => {
            hidden[1].classList.remove('hidden')
        })
}
