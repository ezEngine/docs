#!python3

import os
import re

import Doc

snippets = {}
Doc.SearchSourceSnippets(r"D:\GitHub\ezEngine\Code\Samples\SampleGamePlugin", snippets)

Doc.ReplaceTargetSnippets("./docs", snippets)