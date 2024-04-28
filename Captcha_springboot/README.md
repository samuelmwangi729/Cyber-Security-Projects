#Installing and verifying done using maven
Installation Instructions 
1. Clone the repository from github
2. Open the repositoty using a text editor. In my case, I used vscode
3. In vscode, install java debugger  and springboot extension pack
4. After installation, they will load everyting the project needs
5. Install maven so we can run the springboot project. In my case, it was sudo apt install maven
6. Navigate into the project folder and run the project by  mvn spring-boot:run
7. Open the browser url localhost:8080/captcha/ and the captcha will be generated
8. to verify the captcha, Send a post request to url http://localhost:8080/captcha/verify-captcha/ with the form parameters captcha and value captcha_value using postman
9. You will get the response if you have solved the captcha.