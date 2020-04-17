# -*- coding: utf-8 -*-

string_with_unicode = "ăѣ𝔠ծềſģȟᎥ𝒋ǩľḿꞑ𝙱ƇᗞΣℱԍҤ١𝔍К𝓛𝓜ƝȎ𝚸𝑄Ṛ𝓢ṮṺƲᏔꓫ𝚈𝚭𝜶Ꮟçძ𝑒𝖿𝗀ḧ𝗂𝐣ҝɭḿ𝕟𝐨𝝔𝕢ṛ𝓼тú𝔳<.>/?~𝖠Β𝒞𝘋𝙴𝓕ĢȞỈ𝕵ꓗʟ𝙼ℕ০𝚸𝗤ՀꓢṰǓⅤ𝔚Ⲭ𝑌𝙕𝘢𝕤"
assert issubclass(type(string_with_unicode), bytes)
assert len(string_with_unicode) == 282

encoded_in_utf8 = string_with_unicode.decode(encoding="utf-8")
assert not issubclass(type(encoded_in_utf8), bytes)
assert len(encoded_in_utf8) == 95

encoded_in_ascii = string_with_unicode.decode(encoding="ascii", errors="ignore")
assert encoded_in_ascii == u'<.>/?~'

# We don't know how to represent the data unless all unicode points are available
poop_emoji = "💩"
assert len(poop_emoji) == 4
assert poop_emoji[:1].decode("utf-8", errors="replace") == u"�"
assert poop_emoji[:2].decode("utf-8", errors="replace") == u"�"
assert poop_emoji[:3].decode("utf-8", errors="replace") == u"�"
assert poop_emoji[:4].decode("utf-8", errors="replace") == u"💩"