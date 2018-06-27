#!/bin/bash
# List of emojis
wget https://unicode.org/Public/emoji/11.0/emoji-test.txt

# Spanish translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/es.xml -O annotations-es_ES.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/es.xml -O annotationsDerived-es_ES.xml

# French translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/fr.xml -O annotations-fr_FR.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/fr.xml -O annotationsDerived-fr_FR.xml

# Hindi translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/hi.xml -O annotations-hi_HI.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/hi.xml -O annotationsDerived-hi_HI.xml

# Hungarian translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/hu.xml -O annotations-hu_HU.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/hu.xml -O annotationsDerived-hu_HU.xml

# Norwegian Bokmal translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/nb.xml -O annotations-nb_NO.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/nb.xml -O annotationsDerived-nb_NO.xml

# Dutch translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/nl.xml -O annotations-nl_NL.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/nl.xml -O annotationsDerived-nl_NL.xml

# Polish translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/pl.xml -O annotations-pl_PL.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/pl.xml -O annotationsDerived-pl_PL.xml

# Russian translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/ru.xml -O annotations-ru_RU.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/ru.xml -O annotationsDerived-ru_RU.xml

# Traditional Chinese translations
wget https://unicode.org/repos/cldr/trunk/common/annotations/zh_Hant.xml -O annotations-zh_Hant.xml
wget https://unicode.org/repos/cldr/trunk/common/annotationsDerived/zh_Hant.xml -O annotationsDerived-zh_Hant.xml
