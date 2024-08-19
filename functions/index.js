const functions = require("firebase-functions");

const SENDGRID_API_KEY = "YORU SENDGRID_API_KEY!!!";

const sgMail = require("@sendgrid/mail");
sgMail.setApiKey(SENDGRID_API_KEY);

target = "kwak"
dbRef = "/Recognition/" + target
exports.cloudMailFunction = functions.database.ref(dbRef)
    .onUpdate(( change, context) => {
        console.log(change.after.val())
        const user = change.after.val();
        const name = user.name;
        const path = user.path;
        const message = "Facial recognition system detect " + name
        var text = `<div>
            <h4>Face has been detected ${name || ""}</h4>
            <ul>
                <li>
                Name - ${name || ""}
                </li>
                <li>
                Dropbox path - ${path || ""}
                </li>   
                <li>
                Dropbox Address - "https://www.dropbox.com/home/%EC%95%B1/face1803?d=1"
                </li>
            </ul>
            <h4>Message</h4>
            <p>${message || ""}</p>
        </div>`;
        const msg = {
            to: "woo010487@gmail.com",
            from: "woo0104787@gmail.com",
            subject: `${name} was detected by Facial recognition system detect`,
            text: text,
            html: text,
        };
        return sgMail.send(msg)
    });
