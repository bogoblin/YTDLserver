// ==UserScript==
// @name         Download all YouTube videos
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Tell an instance of YTDLserver to download any video page you visit
// @author       Bobby McCann (bobby@bogoblin.com)
// @match        https://www.youtube.com
// @icon         https://www.google.com/s2/favicons?domain=mozilla.org
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function sendYtDlRequest(url) {
        const params = new URLSearchParams();
        params.append('url', url);

        fetch('http://localhost:5000/download',
            {
                method: 'POST',
                headers: {
                    'Content-Type': "application/x-www-form-urlencoded"
                },
                body: params
            })
            .then(() => {
                console.log("Download successful");
            })
            .catch((err) => {
                console.log(err);
            });
    }

    let currentUrl;
    setInterval(() => {
        if (currentUrl !== location.href) {
            currentUrl = location.href;
            sendYtDlRequest(currentUrl);
        }
        }, 2000);
})();