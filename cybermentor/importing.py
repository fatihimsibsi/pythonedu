#!/bin/python3

# importing önemlidir.

import sys # sistem fonskiyonları ve parametreleri içindir.
print(sys.version)

from datetime import datetime #modül ve modülün içindeki bir kısım aynı isimde olduğu için karmaşık gözükebilir fakat bir modülde sadeceistediğimiz bir parçayı alamk istersek bu şekilde yapmalıyız 

print(datetime.now())

from datetime import datetime as dt # as kullanrak kendi istediğimiz bir isime yoönlendirdik ve çağırıken o takma ad ile çağıracağız 

print(dt.now()) #modülü kullaırken as ile verdimiş olduğumuz takma isimle çağırmış olduk.

