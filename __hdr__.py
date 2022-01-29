### Script Header Maker | v0.1 ######
### Wolf van der Hert | 07 Jan 2022 #
### https://github.com/Woflje #######

import clipboard

hdr_info = {
	"author": "Wolf van der Hert",
	"contributors": "",
	"date": "07 Jan 2022",
	"version": "0.9",
	"title": "Resistor Picker",
	"github": "Woflje"
}

hdr_items = [
	f"### {hdr_info['title']} | v{hdr_info['version']} #",
	f"### {hdr_info['author']} | {hdr_info['date']} #",
	f"### & {hdr_info['contributors']} #",
	f"### https://github.com/{hdr_info['github']} #"
]

if not hdr_info['contributors']:
	del hdr_items[2]

hdr_length = len(max(hdr_items,key=len))
__hdr__ = ""
for hdr_item in hdr_items:
	__hdr__+=hdr_item+"#"*(hdr_length-len(hdr_item))+"\n"

if __name__ == '__main__':
    clipboard.copy(__hdr__[:-1])
    print(f'{__hdr__}\n- Copied to clipboard!')