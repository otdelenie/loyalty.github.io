//настроит страницу пользователя
//сохранить в базе данных имя и телефон, при нажатии на кнопку "Join the loyalty program"
//убрать возможность добавлять новую кнопку при каждом добавлении пользователя


const joinButton = document.getElementById('join-btn');
const logBtn = document.getElementById('log-btn');
const contForm = document.querySelector('.cont_form');
const submitBtn = document.getElementById('submit');
const closeBtn = document.getElementById('close');

const nameInput = document.getElementById('username');
const phoneInput = document.getElementById('phone');

const phonePattrn = /^\+\d+$/; // /^pattern$/gm
const namePattrn = /^[a-zA-Z]+$/;

function saveUserData(name, phone, list_users) {
    const user = new User(name, phone);
    // Here you can implement the logic to save the user data, e.g., send it to a server or store it in local storage
    console.log('User data saved:', user);
    console.log(`Name: ${this.name}, Phone: ${this.phone}`);
    console.log("Username:" + name + "Phone:" + phone);
    list_users.push(user);

    // For demonstration purposes, we will log the list of users to the console
    console.log(list_users);
    for (let i = 0; i < list_users.length; i++) {
        console.log((i+1) + ". User: " + list_users[i].name);
        console.log("Phone: " + list_users[i].phone);
    }
}

let userList = []

// class List_users{
//     constructor() {
//         this.users = [];
//     }

   
class User{
    constructor(name, phone) {
        this.name = name; 
        this.phone = phone;
    }
}

function accauntBtn(name) {
    const userBtn = document.createElement('button');
    userBtn.className = "btn";
    userBtn.id = "user-btn";
    userBtn.innerText = name; // Set the button text to the user's name
    // userBtn.textContent = name; // Set the button text to the user's name
    document.body.appendChild(userBtn); // Add the button to the page
    userBtn.addEventListener('click', function() {
        window.location.href = 'user_page.html'; // Redirect to the user page
    });
}


joinButton.addEventListener('click', function() {
    contForm.classList.add('active');
});

closeBtn.addEventListener('click', function() {
    contForm.classList.remove('active');
    nameInput.value = '';
    phoneInput.value = '';
});

submitBtn.addEventListener('click', function(){
    let name = nameInput.value.trim();
    let phone = phoneInput.value;

     let isValid = true;

     if (phone == '' || name == '') {
        alert('Please fill in all fields');
        isValid = false;
    } if(!phonePattrn.test(phone)){
        alert('your phone number should start with + and contain only digits');
        isValid = false;
     } if (name.length == 1) {
        alert('your name should be longer');
        isValid = false;
    }  if(!namePattrn.test(name)) {
        alert('your name should contain only letters');
        isValid = false;
    }
    
    if (isValid) {
        alert('Thank you, ' + name + ', for joining the loyalty program!');
        console.log(name + '-' + phone);
        contForm.classList.remove('active');
        saveUserData(name, phone, userList);
        accauntBtn(name);// Redirect to the user page
        // window.location.href = 'user_page.html';// Redirect to the user page
    }
});