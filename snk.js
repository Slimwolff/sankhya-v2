// ==UserScript==
// @name         sankhyasul
// @namespace    http://tampermonkey.net/
// @version      2024-03-20
// @description  try to take over the world!
// @author       You
// @require      https://code.jquery.com/jquery-3.6.0.min.js
// @require      https://unpkg.com/hotkeys-js/dist/hotkeys.min.js
// @require      https://raw.githubusercontent.com/wansleynery/SankhyaJX/main/jx.js
// @require      https://gist.github.com/raw/2625891/waitForKeyElements.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js
// @match        https://soldasul.sankhyacloud.com.br/mge*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=sankhyacloud.com.br
// @grant        none
// ==/UserScript==
/* globals jQuery, $, waitForKeyElements */

"use strict";
const $j = jQuery.noConflict();

const port = 5555;
const configEndpoint = `http://localhost:5555/setConfig`;

function getCookie(document, cname) {
    var name = cname + "=";
    var ca = document.cookie.split(";");
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    console.log(ca,name)
    return ca;
}
/**
   * Retorna o JSESSIONID da licença. Note que uma tela com a licença deve estar aberta.
   * Por exemplo, se tu queres a licença mgecom, um iframe (tela) com o atributo src
   * que comece com /mgecom/ deve existir no html da página.
   */
function getLicense(license) {

    let src = [] 
    //get iframes
    let iframes = document.getElementById("viewStack").getElementsByTagName("iframe")
    iframes.forEach(e => {
        src.push(e.src)
    });
    

    return getCookie(document, "JSESSIONID");
}

async function sendAllLicenses() {
    const availableLicenses = ["mge", "mgecom", "mgefin"];
    let configObj = {};
    for (let license of availableLicenses) {
        try {
            configObj[license] = getLicense(license);
        } catch (e) {
            console.log(`Sem ${license}`);
        }
    }
//     await fetch(configEndpoint, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify(configObj),
//     }).then(data=>{return data.json()}).then(n => { console.log(n)});

//     const licensesServer = await fetch(configEndpoint, { method: "POST" }).then(
//        (r) => r.json()
//     );
    console.log(`Client: ${JSON.stringify(configObj, null, 2)}`);
    console.log(`Server: ${JSON.stringify(licensesServer, null, 2)}`);
    return configObj;
}

//let prevIframeCount = 0;
// setInterval(async () => {
//     const iframeCount = $j("iframe").get().length;
//     if (iframeCount !== prevIframeCount) {
//         console.log(prevIframeCount, iframeCount);
//         prevIframeCount = iframeCount;
//         await sendAllLicenses();
//     }
// }, 2000);

function resetCentral() {
    $j("div.AppItem-center:contains('Central de Vendas') + .icon-close")
        .click();
    setTimeout(() => {
        top.workspace.openAppActivity("br.com.sankhya.com.mov.CentralNotas", {
            NUNOTA: "2334",
        });
    }, 1000);
}


function startup() {
    const listaResourceIds = [
        "br.com.sankhya.mgecom.mov.selecaodedocumento",
        "br.com.sankhya.com.cons.consultaProdutos",
        "br.com.sankhya.core.cad.produtos",
        "br.com.sankhya.fila.de.conferencia",
        "br.com.sankhya.cac.ImportacaoXMLNota",
        "br.com.sankhya.core.cad.parceiros",
        "br.com.sankhya.menu.adicional.AD_TGHSQL"
    ];

    let t = 1;
    resetCentral()
    for (const resourceId of listaResourceIds) {
        setTimeout(() => {
            JX.abrirPagina(resourceId);
        }, 1000 * t);
        t = t + 1;
    }
}

function getJSessionId() {
    var jsId = document.cookie.match(/JSESSIONID=[^;]+/);
    if (jsId != null) {
        if (jsId instanceof Array) {
            jsId = jsId[0].substring(11); }
        else {
            jsId = jsId.substring(11); }
    }
    return jsId;
}
hotkeys("ctrl+shift+q", async function (event, handler) {
    let a = getLicense("mge")
    console.log(a)
    //alert(`Licenças atualizadas!`);
});
hotkeys("ctrl+,", resetCentral);
hotkeys("ctrl+shift+,", startup);