import webview as w


u = "https://terminator.aeza.net"

j = """
document.addEventListener('DOMContentLoaded', function() {
    const asideElement = document.querySelector('aside[data-astro-cid-ssfzsv2f]');
    if (asideElement) {
        asideElement.remove();
    }
});
"""

def ij(window):
    window.evaluate_js(j)

def c(u):
    window = w.create_window('', u, width=1200, height=800)
    w.start(func=ij, args=(window,))

c(u)