#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
import json
import requests

# disable warnings
import warnings
warnings.filterwarnings("ignore")

postBody = "\
<xml><ToUserName><![CDATA[wx1c77202393c1c41d]]></ToUserName>\
<Encrypt><![CDATA[1Kfw3aYF5AlKbQZ9jBldvkMIadHnZfkEIm+Uw/0JCXAg6KNaP1Ghaz4eeCmQntUB7U0/zHfB8x7YZrTVl8Vh0WO3GCT+68gb1e0Qza27no/b+L0+elFbZbZpHHwrbaTlqOPmoFxhyvsXs4Nzn6zRL5mP4jjcc3cd0Ba6DXMY4IMvsWdRtrdiqX6H7Blrzuy3A3GhLihEkrBN1lCfsZyoUkkH+oGklmfxaj+ki+vx+g1NhNhPl4efqvFLzjdcJJUi5LIMsVP+7joKRBUQIy79wufW3TqRsmIuexcl9xxMmBwXba1bvu+BjQe6kDWVgfIC5TFx8r0pg0Ti/WahkzE8Bc4JCbbARWT8kRsyf5xBKjjhq19gAkZpH1maUwtfVCxwhhsmo9VA4U2UXanPbxrpvtzTIyciDmqMcHsosm8Nb6AdvpGwRy4zMpylvQN0NlNEwJCIsXXcrWMLCNM83B8ZHw==]]></Encrypt>\
<AgentID><![CDATA[0]]></AgentID>\
</xml>"

addOn = "/?msg_signature=92264009fb7a515ba6e5d4c8b321cde856cb32be&timestamp=1448532035&nonce=150534080"
Theodolite_URL = "http://127.0.0.1:8000{0}".format(addOn)

def post():
    requests.post(Theodolite_URL, data = postBody)

if __name__ == '__main__':
    post()
