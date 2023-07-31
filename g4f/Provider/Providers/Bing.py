import os
import json
import random
import json
import os
import uuid
import ssl
import certifi
import aiohttp
import asyncio
import time
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://bing.com/chat'
model = ['bing','dall-e']
supports_stream = True
needs_auth = False
working = True

cookies = ['MUID=2CDF36CF1BED6F453AA325951AFF6E9A; MUIDB=2CDF36CF1BED6F453AA325951AFF6E9A; _EDGE_V=1; SRCHD=AF=UNKSBD; SRCHUID=V=2&GUID=7E766696152D40CDB1078CC2B9E1CE95&dmnchg=1; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=0847c270-ac5f-4d28-af4b-aef32a9d3e34; ANON=A=645B9833C1A53C9364F261D2FFFFFFFF&E=1c9e&W=1; NAP=V=1.9&E=1c44&C=akcivvAqGgPkamNz0ldEfRw_bfFGYEcsNusia3ITSXF8b1W3UWv3tA&W=1; PPLState=1; KievRPSSecAuth=FAByBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACE2BEL4egNsbMASW9UIQXfqutBopNvzNle6zaYLlNl/hsL2Jac3h4MBVhCQ88oz+vrbCeEcqxZ368alFZ8g5fhmyr6Xrc6F12hY60z8TatM3T7OnV5MYxTTkhHfKylq36sgGUe6EhZ8uYwsarjq/YJg2lNgyi6tbnPRyXi1+4niuEBI3V3dazwb9y57mJZDU1OOIqL25q2cYI0/LnFpFUcwF54fP1t2dh2OLT/fZVsR8tyKtk9tfGfifyTRG5kbsXih1FnlL3s6V2yFkRDGWe7sgWZncFOpT4tIRCgCYwNHuQ23bkuqSj5Ymk7r2v/tg8UlQuqxM3GabGBasY/VWrFav+kTR/rh0yKQdbkVMQlBVoiFnkHip+uM5yS+qlwIuGSJfEHjZ+HPpgrSsSf3ze7agIA0icWf9bqKOBDz8JIAxQPuPKiaPx1PUyQ7gqmWdR/42tnzMj5PtZmLMw8ku95Z8WtnFlG2L6Er4V3FdbU1Wiyo0oxMmYYc64T8xYxS9dUv1Coq+nvBetzHgC0EZM4JNwPGTtpKg96dNW3aNvWq1iPJiRmgPaku53fw8IfjikJwukWHWi1g2074SSgFx8xY/5iT36ok68uUfuxYCUMezNC+g2NOwcmIsjjnT2W8HmbUWiWVVINohqQVPKd4qJ/82LN3FSoEFbaMJV57jN9J11RaHkDjoVhBmgMFNPLkFNy8sbww+4mjf4xp6Jh6vI1GdvjwHFgcy0zIp+M7jvsb/C2sutvp6yoPw39IhSYiGDhs8QyOqc2vHZBOuvWKa0tEC/Te265FVIwHNKGbT4PiTfzSNI0H/Nxcfm7GfJ6fF4mSPR+HFHD8PFopymbOTrfCgiPfBFAphiG1i3dmll0jgxVeNsat19U7xoDj96bhhQokXSwNzNcO2erYzCmXfVOsywDf6zHF+kjIz8I4+ULy3EVzzEbhCfzGMMnlMEvNoLdfKh0phqGO0qhaI7+LJ3vtTIMSDBy7L1VQdD7baTOxiXhdWsinIxA/RWyPE9il7hsETU43bEw1fj/QuwbZqJoMHu2Rp7EF8Knlum9vsg6NmYsLOEYgt+bkGNszVB/J2SJak8NkkRxXnHP/MIHTjc8ymb0CuNFmyZ4z92nfbcM2ZJcHWQdD+sNEyaChp2QLw4Fhtvpqw9ws2tIOH2V3Ge0Av4NzQ2JYvCvPnVlqaxWrdBc3lN7DH+z5rcy/25MFZjkW7az+784QDJnpjKeHZoE27qOCKCnAXVD8UOklfZMmMitqLtSU3u2M5g+d9UtWtLiIWbPP9AwRXu5CFmRx1RxeHL8PwXyo2+Cn8/nrtgJs0Y7MDBAXFb0mdVg98E6Ma17GCix5X2at8egCzl3EOR7mJcCFAT2NQMrAKSYwIyqHWF8vkddhn9Y0TRUlpIMjtrg5ejxH8dTJWLl/GDGAuZfMvZWerMArH0NC+FADNvDoxBXi+LAQQ0N+6AtAsWcRD3A==; _U=1iz6DwIeSr1uHIkU7I-pSFbPfAsMnC7wTKjkT0Cbo4-T-Mk8T8PkzDZDMIS1DsVtXhPi5q_GP_LKV8wlaXVOFGydDRQtLcyyvHDgfFHXLZAJo3kaDglWq4zamZopeM0_AWT0mS3LmzkmMO99ng1OoM4E3yqoJCQhXmVJN_hhXjz1x-1trQyfG4yGNRUoG9i8I9FMchwGIapFSdwmcGBGtbw; WLID=E29T04WkWyMhLD8Qab7oErkSwFZe4vAjSWJy7CtfhTctmsR8B5upFhh0nZ6PDldK/N4bU7cpEVO70kVJ7CntuY+qACiq44rIU6y9YQjkzew=; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNy0yNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NH0=; SnrOvr=X=rebateson; USRLOC=HS=1&ELOC=LAT=43.710304260253906|LON=-98.48551940917969|N=%E6%99%AE%E6%9C%97%E9%87%91%E9%A1%BF%EF%BC%8C%E5%8D%97%E8%BE%BE%E7%A7%91%E4%BB%96|ELT=1|; ABDEF=V=13&ABDV=13&MRNB=1690532475452&MRB=0; cct=AtPNzx1w_FSdkdsToLIYWEAeYOSTBrWagktAUqprkJ4lHzXsnPShx3j9XY40Xosyc3OzoBdRnguN8BPxLnkc9A; SUID=A; _EDGE_S=SID=164EE26E8F14621B0A67F1338E4563C7; WLS=C=0911dcf849c41c02&N=Smith; SRCHUSR=DOB=20230726&T=1690604434000&POEX=W; _RwBf=ilt=1&ihpd=1&ispd=0&rc=67&rb=67&gb=0&rg=0&pc=67&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=4&l=2023-07-28T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=4107&s=2023-07-24T15:46:31.7545551+00:00&ts=2023-07-29T04:20:36.6769802+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&dci=0&W=1&r=1&mta=0&e=fPeEcp-5tY4SeU5r6IWp5lxG3K3Awj4xbTrEHar-qoblAB9rKGwwgQz2psjo2_zrpeQfoTFCatplWNHqWqaqqA&A=; _SS=SID=164EE26E8F14621B0A67F1338E4563C7&R=67&RB=67&GB=0&RG=0&RP=67; GC=AtPNzx1w_FSdkdsToLIYWEAeYOSTBrWagktAUqprkJ6p7gca286Aa5NNb7vGXDonDWfq0k-qY8f2iUCpcUyGTA; ipv6=hit=1690608040581&t=4; SRCHHPGUSR=SRCHLANG=zh-Hans&IG=241DC1B763D54572AB1481C331F4892F&PV=10.0.0&BRW=HTP&BRH=M&CW=927&CH=754&SCW=927&SCH=5800&DPR=1.3&UTC=480&DM=0&HV=1690604437&WTS=63825944964&PRVCW=927&PRVCH=754&EXLTT=8','MUID=37F7249B8FCD6EF92BB037C08EE36F48; MUIDB=37F7249B8FCD6EF92BB037C08EE36F48; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=95335F81D9C046BCB2754DA32F69B849&dmnchg=1; _UR=QS=0&TQS=0; ANON=A=7F66B4E7DCD4F4008ADA6E1EFFFFFFFF&E=1c9f&W=1; PPLState=1; KievRPSSecAuth=FAByBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACCF/Ue3zc09gMAQrV8eDFJQjg32yqeHgBh1mqpdAT+0KuiphUvHoo6NjAfuaZ3YrdSFFABWJNSW65kVwVhb87N/O9+3WOnAVE8NmWYHn05oH7XdU7O0N8Bebouh3cLnW1OmnU0A9/tZAhwdCOiUnyebCiHc/Glm9XqgHt8puX/53k0Aq5/9vNCu2zjHMrnA7FKjaulRnytyE3xsPNlpTRhP4P8nCaig9rcjVp1Eqq61xg4KXmIivdgBjfvk5CBEwwJA7nM+JFEha+TJx51Tj2xuxsqRDOyTvjD8LXf+LwV1DOfOHdiK7l0WJKdEzhDZE1DjPf+Dcp89yn1GVrHsmjdhtRmmkLDpHk0jOZP34VIcOtL7I42Kd/CKh5IJQ4+Vouib7Iuq0vmxemjTnTcbswH48Gnvb2RKsHblh6Xmcb+i0kKpu+2DgnSCiQi74ZZjElY77podiOUuVhnWS0Jc5eioJ33es2kdWMRo3BoWEAW+hnzPV9b0oOUaKANXDTgoTnmqyxV+AWAxADnnL7AmFT19onokRhdsKaM6iS6i9W55o2Sz3vTW84rgLe7pCwuxuEE1g595kSQpat0FZz4OzfvdGP1RihbVM0svLBPWvaeSktJYmVsOQ3bIQOVN+zAY/sNcGVDWskJWCqjpRDomEDXC9HSrMVg+HEr/W/+hk6ZX3oipYFOr7mgRtSz7jHDvjwzYaJLLH0FETRjSKj2N/ohv8MfpIXhEkA5wm8fHk8hw3GrhGuljEAyPO7NftcKr1UhhB23a9ZOwM4bR3u+FIk/A71WVNu+bEytwpKML05wMJy6fGzeMW8UF+epWEfZGDsUAPTsLYayVolpB4e8By6YMCvUIVjLdd4/cc/NLRvs216IxIEFhqra953vC5NzP/Cwz2mkgCmcduh6rgv8yhgICQ5tOy3IPuzJPoBzpWuBfJ51q/Dyf8xF4oSvrLmPZEz30w+uaFLa3wsmztsG+mIUIKpBbujv5FB6uEijcem0Sa4t3sQbMQHPiDUkTPnEZSbzKorMYYwQeIjrWkUojacPGOp95DkfEWlveyjfzX9ArBhWd/uA2Gkml6BQAHdArU7HTGBko0fyefuZ4qD+q7Qyt0+QprvwDFDX0HxwybtQB9zJBB91M+mOCEO/twT9SCI29MeBdjhHYQhhPPJMmbkzb7Nb/aeMtUV+UmKDZdC6Q8VRiTLyHAT+RAOHZaTjTznC+ShzP2g8cX8Cmi8QHcIxmazAZor6ZEjBSysM/7EBmw0aRZ6VhTiFGbFp34QvR42dZvI/xJav5vDETkUkA4Yfzep8UScNgJXjZqu+r1b7VPfmMGuOprhGn7criB9XyLoabsvmz7hoLyb030Y7Y+CljHF3v4+bSoGcL/YPG1mXoiMtOYEKoNaiA1dN876/eL1X5XJBZKkY+G6sDfPJfZH3Zp9OntsDdxnYEJFADDlTGRTqRKLopRgvmMPveoYj/7tg==; _U=18zdJpcOM6t1jfs6O7pPyJtaF1Pcla2T-xnsUFKmFGpENRX3wpzRKavRSfYLpJdb9OxDGD5fqv8eRTd5YMM0IbTPFH0RoW2E8E8YbbI8QEYgx9-EGh2BCpbQhE0ataHVnO4kN3QZj-flMnj5YK-xbbfg4-faSeBgIm4l12jVGz06WPI1IOwU2EU37ap8gusm6zdACsyTNY_qN-KK7gnQwjeoEHcw0lJAvh7N2fEcZTvI; WLID=F7198T5aDAqsbhT1lyRdcQX2oDHdv674MHw09DTfeIbZ3ynu8AxwEFvIG4MZaIUw15A+sluvqJsrYQGb2N/cvjr5FmPjjs9LTK6b5atYG8M=; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNy0yN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6M30=; USRLOC=HS=1&ELOC=LAT=43.710304260253906|LON=-98.48551940917969|N=%E6%99%AE%E6%9C%97%E9%87%91%E9%A1%BF%EF%BC%8C%E5%8D%97%E8%BE%BE%E7%A7%91%E4%BB%96|ELT=1|; SnrOvr=X=rebateson; ABDEF=V=13&ABDV=13&MRNB=1690532539329&MRB=0; SUID=A; WLS=C=84f89dfd83bfd741&N=Smith; _EDGE_S=SID=027784E1E18263852BF897BCE09062E0; SRCHUSR=DOB=20230727&T=1690604562000&POEX=W; _RwBf=ilt=2&ihpd=0&ispd=1&rc=0&rb=0&gb=0&rg=0&pc=0&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2023-07-28T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=1799&s=2023-07-27T07:10:22.7171259+00:00&ts=2023-07-29T04:22:46.6627522+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&dci=0&W=1&r=1&mta=0&e=GJe87IrXcmQRHN3bICBR-gNbDsx4TP7q-rQrUEYM0cuvsL8EgWetIvrL5Xz9dZdIhUKT27u8U56UwMYR4KwRRQ&A=; _SS=SID=3C8878AC6DB76CD822456BF16C006DBC&R=0&RB=0&GB=0&RG=0&RP=0; ipv6=hit=1690608168189&t=4; GC=-tMw9SSxs052FGdJoWta7F_KycXU7Jm-ax_eoNXKn8RzeDY9lFHndGmr7l2SaxzUQWXdH2fySLau-GZwKHnh1Q; cct=-tMw9SSxs052FGdJoWta7F_KycXU7Jm-ax_eoNXKn8TxYPHORoTMPn9k_VjT7OkxpJqm1JqTFZSNJQoIdLFqeQ; SRCHHPGUSR=SRCHLANG=zh-Hans&IG=177DB3DD380D4799B33BFB549A75E2A1&PV=10.0.0&BRW=HTP&BRH=M&CW=927&CH=754&SCW=1164&SCH=3795&DPR=1.3&UTC=480&DM=0&WTS=63826037984&HV=1690604567&PRVCW=1482&PRVCH=754&EXLTT=6','MUID=1AB8B5F154E660D1186CA6AD557F6112; MUIDB=1AB8B5F154E660D1186CA6AD557F6112; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=AF3645A9D6044A6EB5EA6C23A00AEAFC&dmnchg=1; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=54b32a89-dd37-4f54-8616-7df466a80a3b; ANON=A=4648389BAD678A4DC268B12FFFFFFFFF&E=1ca0&W=1; NAP=V=1.9&E=1c46&C=QYC-TsNC5BDgfCTL8z2ibQf0BftAOaZ2EL-fRA6OmPWW4RCx-V175g&W=1; PPLState=1; KievRPSSecAuth=FAB6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKbjerwSPUbLOAS2nVP9Zbn9iq0ygXK1vrHWLrvU9hUtPkd48YK/JVNcoFgZg1vpV9xCv87kRs72ryCSX7vIRR9kIvtPMKR+ShvRLB1Ty5EI/mrKw6dPgtyZ5aaO4xL/gXi1YXubz+Z2dIgeTO5dCMrMXVYTz3mpFaXIG3p9Q0GYSLf6yfLqJh2VhDo4XzLSIIK/sd8QsxdngxCUS9pKHuOusk3OWVUMOV2szgkyOFNaewkem30UY0WPO5m/L5BTy/0hBEkTXMbD19Q4rDTmVKnUVuEcTNC34mm7DdHZ5WIZsWt53o6nAdqbf7R6Rl2wGUUFCG6avMDkcMQMRfI69+6bXPaB88umo5nZAR3IJhhHy+F5e6HNOzH1IlqrTQAqtmmjrRg6tINKPXqDaq3c+a7jM3yZ82f9d2wkpb/Q8b2E6j72dDJBhQ9+mJoqJERHKW8oLz1IIVH7HiASjFAzhq0q3nreQVHrc8rffB9aHSOLYL3eh8hqkHg2vW5CZijZrHcawfm/bp2e74QxMZVXX7nzfLtfZgUEWpkFa06p77irDZCSQa409yolXkXYhtfNz4uKHbmPilBImUYhufU/J4oFEDBZ6qv0B9BnXyPS7EF5HL7w6gN5C1bdRPQuXLd+J7DNikLV+uAlLnAf7XE21eZWoT4eUlJc7Woj//4rwoAieh3cXfbIYs5iHhLExCzqu87ksBIMGgkqQuHUTJT5DvPP6orAIXXIFAsr/W9T1QtxIsLZFEk8gFpjMbfGHffYthj0R30lmKrwpVRI84g6+DxzhutNMBvthqapSdrxjNYOZHk5vflERE/j1EaPuN/szp41xZL80B1LRO5XQJrolVP/9Hg2jdRk4MNREq3dLVwQM3MmHsfe/SgHqnyvjqwPFdehpVbvPak7JPh7PVFWofsUc3l2D1ijdWQMTZ5neLVjt2lEVlxW99VCllnlvUSyqUe51QCCnNt1+XGCE8b9oFct+FyG+V+zRGGVfUDTGPWaqcyN+eBaZAH7tiBaZCtAarNUGs/+4DUanbZ64S5mJqvkB7Rfck5cUgayXDMiMNsDwMhhWOOliAqq7UwDCRnRZ5dpk0cuBxHNzoUtAOloOZDPuKRC/nWlhV1s8DDP/e+RF00AWcHhLDub3VKWix2LD9eZmLB7kaiIapaGxQ7famTXP3EBp2nwbhlMbYzRbLxi4XgO/4DLuPUo+dxpQQotQ693fJr67KqiSmA+qjBzPegPUlOoNhyGzIuA1S/ogjJDxVsdL/I1JYUxGag8rW/A7SdGWunwzuspd/Lxj70FDER4G5/JOPPPmu22HSQwjjQmdkHDANJkhk1dZ2Mnw4FDQxlqNIVgRUmsIXTgte7smnhQnq++FfcsLcLlFLj+UvI3WYRTQESmmxZMLAKJiHaun+AOCksSWxuXn6fklncJakTQ+uadoZvpGNZA2SWA/GprNB4UAJOf/b/m58BhVp8FkAHqfwtvJ//I; _U=1RRT3N9897Unc7lqwcayUJRg0weqoRK6E-SaDZRxU1pKFMclk5dWrUDf6-x3SR65fFc6E6rjcAjteB9mVB7VdDIzmBnYVJAOqaGSEYye779KvpIUg3_eT0o3E1fuAYYjD-iiQxMwd8FCKLUAEND3lix-FhQ6EW3xCnMH5ofgI8Sy_yEX9g4Ehr-Fp6DUINSYIewZx_B_b1ax96fCKIHtoIJFPqWDJExCU9V20QP0vShA; WLID=5HKjNyzHgwVTvOJiZUJHhRCklFwQ4ZXLJJceSE+qUcLyP9u3YEBfXva8bI3wUs+JM5iGsAycmq0o1trJrLmvq/GMUcYntHG5viNrJPTwm5M=; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNy0yOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NH0=; USRLOC=HS=1&ELOC=LAT=43.710304260253906|LON=-98.48551940917969|N=%E6%99%AE%E6%9C%97%E9%87%91%E9%A1%BF%EF%BC%8C%E5%8D%97%E8%BE%BE%E7%A7%91%E4%BB%96|ELT=1|; SnrOvr=X=rebateson; SUID=A; _EDGE_S=SID=13A3D83641176C13042DCB6B40BC6D4E; WLS=C=d5accf9efdba999e&N=Smith; SRCHUSR=DOB=20230728&T=1690604674000&POEX=W; _SS=SID=13A3D83641176C13042DCB6B40BC6D4E&R=0&RB=0&GB=0&RG=0&RP=0; ipv6=hit=1690608283881&t=4; cct=Km5OnV7eaN4oiWil_hvlJzV-PnLeJYnPXh9Vqy9Dyf__yp_OzsfQ_63jJKvCib8K74n1_9eGhUW8xIe7ESJm_A; ABDEF=V=13&ABDV=13&MRNB=1690604710476&MRB=0; _RwBf=ilt=3&ihpd=2&ispd=1&rc=0&rb=0&gb=0&rg=0&pc=0&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=4&l=2023-07-28T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=5015&s=2023-07-28T03:49:25.0212949+00:00&ts=2023-07-29T04:25:12.3038594+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&dci=0&W=1&r=1&mta=0&e=5hGuvH-hgROgFrAFCyoprGS3tojdQpS-9dprbxKJNPJf5adOY1BMnPReepJYVlCsjKVDlVgwBQSEBQYXrjykKNh4LPcOEPxOqKQ9fMQDo_w&A=; SRCHHPGUSR=SRCHLANG=zh-Hans&IG=A6F1DD36E2E4449090EBC3B4F244A9B0&PV=10.0.0&BRW=HTP&BRH=M&CW=927&CH=754&SCW=1164&SCH=2643&DPR=1.3&UTC=480&DM=0&WTS=63826112199&HV=1690604714&PRVCW=927&PRVCH=754&EXLTT=7; GC=Km5OnV7eaN4oiWil_hvlJzV-PnLeJYnPXh9Vqy9Dyf-XQIULVApCO45kebIJBakbfE_P68YcvgNWtVzth_FNZg']
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())


class optionsSets:
    optionSet: dict = {
        'tone': str,
        'optionsSets': list
    }

    jailbreak: dict = {
        "optionsSets": [
            'saharasugg',
            'enablenewsfc',
            'clgalileo',
            'gencontentv3',
            "nlu_direct_response_filter",
            "deepleo",
            "disable_emoji_spoken_text",
            "responsible_ai_policy_235",
            "enablemm",
            "h3precise"
            # "harmonyv3",
            "dtappid",
            "cricinfo",
            "cricinfov2",
            "dv3sugg",
            "nojbfedge"
        ]
    }


class Defaults:
    delimiter = '\x1e'
    ip_address = f'13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}'

    allowedMessageTypes = [
        'Chat',
        'Disengaged',
        'AdsQuery',
        'SemanticSerp',
        'GenerateContentQuery',
        'SearchQuery',
        'ActionRequest',
        'Context',
        'Progress',
        'AdsQuery',
        'SemanticSerp'
    ]

    sliceIds = [

        # "222dtappid",
        # "225cricinfo",
        # "224locals0"

        'winmuid3tf',
        'osbsdusgreccf',
        'ttstmout',
        'crchatrev',
        'winlongmsgtf',
        'ctrlworkpay',
        'norespwtf',
        'tempcacheread',
        'temptacache',
        '505scss0',
        '508jbcars0',
        '515enbotdets0',
        '5082tsports',
        '515vaoprvs',
        '424dagslnv1s0',
        'kcimgattcf',
        '427startpms0'
    ]

    location = {
        'locale': 'en-US',
        'market': 'en-US',
        'region': 'US',
        'locationHints': [
            {
                'country': 'United States',
                'state': 'California',
                'city': 'Los Angeles',
                'timezoneoffset': 8,
                'countryConfidence': 8,
                'Center': {
                    'Latitude': 34.0536909,
                    'Longitude': -118.242766
                },
                'RegionType': 2,
                'SourceType': 1
            }
        ],
    }


def _format(msg: dict) -> str:
    return json.dumps(msg, ensure_ascii=False) + Defaults.delimiter


async def create_conversation():
    for _ in range(5):
        create = requests.get('https://bing.lemonsoftware.eu.org/turing/conversation/create',
                              headers={
                                  'authority': 'edgeservices.bing.com',
                                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                  'accept-language': 'en-US,en;q=0.9',
                                  'cache-control': 'max-age=0',
                                  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                                  'sec-ch-ua-arch': '"x86"',
                                  'sec-ch-ua-bitness': '"64"',
                                  'sec-ch-ua-full-version': '"110.0.1587.69"',
                                  'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
                                  'sec-ch-ua-mobile': '?0',
                                  'sec-ch-ua-model': '""',
                                  'sec-ch-ua-platform': '"Windows"',
                                  'sec-ch-ua-platform-version': '"15.0.0"',
                                  'sec-fetch-dest': 'document',
                                  'sec-fetch-mode': 'navigate',
                                  'sec-fetch-site': 'none',
                                  'sec-fetch-user': '?1',
                                  'upgrade-insecure-requests': '1',
                                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                                  'x-edge-shopping-flag': '1',
                                  'x-forwarded-for': Defaults.ip_address,
                                  'Cookie':random.choice(cookies)
                              })

        conversationId = create.json().get('conversationId')
        clientId = create.json().get('clientId')
        conversationSignature = create.json().get('conversationSignature')

        if not conversationId or not clientId or not conversationSignature and _ == 4:
            raise Exception('Failed to create conversation.')

        return conversationId, clientId, conversationSignature


async def stream_generate(prompt: str, mode: optionsSets.optionSet = optionsSets.jailbreak, context: bool or str = False):
    timeout = aiohttp.ClientTimeout(total=900)
    session = aiohttp.ClientSession(timeout=timeout)

    conversationId, clientId, conversationSignature = await create_conversation()

    wss = await session.ws_connect('wss://sydney.lemonsoftware.eu.org/sydney/ChatHub', ssl=ssl_context, autoping=False,
                                   headers={
                                       'accept': 'application/json',
                                       'accept-language': 'en-US,en;q=0.9',
                                       'content-type': 'application/json',
                                       'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="110", "Chromium";v="110"',
                                       'sec-ch-ua-arch': '"x86"',
                                       'sec-ch-ua-bitness': '"64"',
                                       'sec-ch-ua-full-version': '"109.0.1518.78"',
                                       'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
                                       'sec-ch-ua-mobile': '?0',
                                       'sec-ch-ua-model': '',
                                       'sec-ch-ua-platform': '"Windows"',
                                       'sec-ch-ua-platform-version': '"15.0.0"',
                                       'sec-fetch-dest': 'empty',
                                       'sec-fetch-mode': 'cors',
                                       'sec-fetch-site': 'same-origin',
                                       'x-ms-client-request-id': str(uuid.uuid4()),
                                       'x-ms-useragent': 'azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.0 OS/Win32',
                                       'Referer': 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx',
                                       'Referrer-Policy': 'origin-when-cross-origin',
                                       'x-forwarded-for': Defaults.ip_address
                                   })

    await wss.send_str(_format({'protocol': 'json', 'version': 1}))
    await wss.receive(timeout=900)

    struct = {
        'arguments': [
            {
                **mode,
                'source': 'cib',
                'allowedMessageTypes': Defaults.allowedMessageTypes,
                'sliceIds': Defaults.sliceIds,
                'traceId': os.urandom(16).hex(),
                'isStartOfSession': True,
                'message': Defaults.location | {
                    'author': 'user',
                    'inputMethod': 'Keyboard',
                    'text': prompt,
                    'messageType': 'Chat'
                },
                'conversationSignature': conversationSignature,
                'participant': {
                    'id': clientId
                },
                'conversationId': conversationId
            }
        ],
        'invocationId': '0',
        'target': 'chat',
        'type': 4
    }

    if context:
        struct['arguments'][0]['previousMessages'] = [
            {
                "author": "user",
                "description": context,
                "contextType": "WebPage",
                "messageType": "Context",
                "messageId": "discover-web--page-ping-mriduna-----"
            }
        ]

    await wss.send_str(_format(struct))

    final = False
    draw = False
    resp_txt = ''
    result_text = ''
    resp_txt_no_link = ''
    cache_text = ''

    while not final:
        msg = await wss.receive(timeout=900)
        objects = msg.data.split(Defaults.delimiter)

        for obj in objects:
            if obj is None or not obj:
                continue

            response = json.loads(obj)
            if response.get('type') == 1 and response['arguments'][0].get('messages',):
                if not draw:
                    if (response['arguments'][0]['messages'][0]['contentOrigin'] != 'Apology') and not draw:
                        resp_txt = result_text + \
                            response['arguments'][0]['messages'][0]['adaptiveCards'][0]['body'][0].get(
                                'text', '')
                        resp_txt_no_link = result_text + \
                            response['arguments'][0]['messages'][0].get(
                                'text', '')

                        if response['arguments'][0]['messages'][0].get('messageType',):
                            resp_txt = (
                                resp_txt
                                + response['arguments'][0]['messages'][0]['adaptiveCards'][0]['body'][0]['inlines'][0].get('text')
                                + '\n'
                            )
                            result_text = (
                                result_text
                                + response['arguments'][0]['messages'][0]['adaptiveCards'][0]['body'][0]['inlines'][0].get('text')
                                + '\n'
                            )

                    if cache_text.endswith('   '):
                        final = True
                        if wss and not wss.closed:
                            await wss.close()
                        if session and not session.closed:
                            await session.close()
                            
                    yield (resp_txt.replace(cache_text, ''))
                    cache_text = resp_txt

            elif response.get('type') == 2:
                if response['item']['result'].get('error'):
                    if wss and not wss.closed:
                        await wss.close()
                    if session and not session.closed:
                        await session.close()

                    raise Exception(
                        f"{response['item']['result']['value']}: {response['item']['result']['message']}")

                if draw:
                    cache = response['item']['messages'][1]['adaptiveCards'][0]['body'][0]['text']
                    response['item']['messages'][1]['adaptiveCards'][0]['body'][0]['text'] = (
                        cache + resp_txt)

                if (response['item']['messages'][-1]['contentOrigin'] == 'Apology' and resp_txt):
                    response['item']['messages'][-1]['text'] = resp_txt_no_link
                    response['item']['messages'][-1]['adaptiveCards'][0]['body'][0]['text'] = resp_txt

                    # print('Preserved the message from being deleted', file=sys.stderr)

                final = True
                if wss and not wss.closed:
                    await wss.close()
                if session and not session.closed:
                    await session.close()


def run(generator):
    loop = asyncio.new_event_loop()
    gen = generator.__aiter__()

    while True:
        try:
            next_val = loop.run_until_complete(gen.__anext__())
            yield next_val

        except StopAsyncIteration:
            break

    #print('Done')


def convert(messages):
    context = ""

    for message in messages:
        context += "[%s](#message)\n%s\n\n" % (message['role'],
                                               message['content'])

    return context

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    if model == 'dall-e':
        HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "referrer": "https://www.bing.com/images/create/",
        "origin": "https://www.bing.com",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edge/110.0.1587.63",
        }
        params = {
            't':int(round(time.time() * 1000)),
            're': 1,
            'showselective': 1,
            'sude': 1,
            'kseed': 7500,
            'SFX': 2,
            'q': messages[-1]['content']
        }
        r = requests.get("https://bing.lemonsoftware.eu.org/images/create",params=params,headers=HEADERS)
        try:
            id = urlparse.parse_qs(urlparse.urlparse(r.url).query)['id'][0]
        except:
            yield 'Image generation error. This may be because your image is illegal or our service has malfunctioned.'
            return
        image_urls = set()
        t = 0
        while len(image_urls)<4 and t<60:
            time.sleep(0.5)
            t += 0.5
            r = requests.get("https://bing.lemonsoftware.eu.org/images/create/async/results/"+id+"?q="+params['q'],headers=HEADERS)
            soup = BeautifulSoup(r.text, 'html.parser')
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                src = img_tag.get('src')
                if src:
                    image_urls.add(src)
        if not image_urls:
            yield 'Image generation error. This is because our service has malfunctioned.'
            return
        for img in image_urls:
            yield '![]('+img+')'
    else:
        if len(messages) < 2:
            prompt = messages[0]['content']
            context = False

        else:
            prompt = messages[-1]['content']
            context = convert(messages[:-1])

        response = run(stream_generate(prompt, optionsSets.jailbreak, context))
        for token in response:
            yield (token)


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
