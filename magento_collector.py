#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# October 2016
"""Magento Malware Identifier"""

import os

IDENTIFIERS = {
    '2sinlesspleasure.com.js': """""",
    'amasty.biz': """String['fromCharCode'](118,97,114,32,115,110""",
    'amasty.biz.js': """var x="t_p#0.qlb#0.#1Blsj""",
    'americanwineclub.se.js': """window["\x64\x6f\x63\x75\x6d""",
    'cloudfusion.me.js': """jQuery(function(t){t("button").on("click",function(){q="h="+window""",
    'gate.php.js': """var se=false;setInterval(function()""",
    'grelos_v.js': """var _0xc188=["\x68\x74\x74\x70\x73\x3A\x2F""",
    'grelos_v_simple.js': """var grelos_v""",
    'infopromo.biz.js': """var snd =null;
window.onload = function () {
    if((new RegExp('onepage'))""",
    'jquery-code.su-charcode.js': """<!--UPS delivery code-->""", # this file has another phrase in the js that could be used to identify files
    'jquery-code.su-multipacked.js': """var lII='=oQKpkyJ8dCK0lGbwNnLn42b""",
    'jquery-code.su-multipacked.js_EXPERIMENT1': """var lII=""",
    'jquery-code.su-multipacked.js_EXPERIMENT2': """=oQKpkyJ8dCK0lGbwNnLn42b""",
    'jquery-code.su.js': """var fa3b79b10153ce22c599aa4c035e421b3={
    snd:null,""",
    'js-save.link.js': """var _0x7539=["\x6C\x6F\x63""",
    'mage-cdn.link.js': """var _0xe94f=["\x70\x5F\x6D\x65\x74""",
    'megalith-games.com.js': """function frm_fill(e){""",
    'ownsafety.org.js': """function jj(e){""",
    'returntosender.nl.js': """var _0x1137=["\x63\x6C\x69\x63\x6B""",
}

identified_domains = {}

for identifier in IDENTIFIERS:
    identified_domains[identifier] = list()

for root, dirs, files in os.walk("."):
    for html in files:
        if html.endswith(".html"):
            with open(html, 'r') as f:
                for identifier in IDENTIFIERS:
                    if IDENTIFIERS[identifier] in f.read():
                         identified_domains[identifier].append(f.name)

                f.close()

