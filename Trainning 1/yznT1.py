
#q='44x8kuk{d8F499uxu}9a{89c98gnnd8hnkk{kcx8Fjmxu8}uhhxjc9kk4}8xxd}hanmn}}xhmmm8mmF	}a98mc8k9unlnu4u49xu99hg8nlcm9ncn}}kcch88unc89x89m88hk}9dug}8n9ldmakku}ux9mhj9lmh}}cgu984x9cxaac}xkuh8l4jmmdxd}kj88u4ukdcmdm}n4kcxmx{jj}9m8m}98}hmdn}9k4aFux}m8{uk8xcn{mum8uxxn9}dagm9cu8j8u{mjhk9uk9{hjjudxgxx89du8m{kx8{}98mccauj99mkkF}8mmxkg99}h8kx8uu}k9mmkjkgu44x8u}xjnc9u}ck4mnkm4jka}8jkj{c}gm}94mku9}a}ng8m8k	n44{8m9jum}8adgmuxu}mln{xgl98udjdkan}4dg4cg}jax}}x4gkhnkmjx9ckd}hujjmxx}cmd}c}x}j8u9c}g8xcmjj9ncuunmk8u{}m}}ukjj9jxh}8x4nu8k}duu49mcu}9mcdu8cx4}9l88n}{a}4u8mmhxj4c9n48mju}juu}u8u}}x}4u889844munukm9c}x9m4kduu8uun48}n8Fx9dk888{8}}}9auu48}4x488mukulnxx8k9{jmaujux}g88alu4}}4dgxu}Fuua8xng9m8gnh9Fumcn{9xhd4u4d9kxd8dk8md88m}gm}944j{k4898h9{md9mxk}ux9kxd8xuagmhc48n8}k}{xclm4{8jk4mcndngmxxxx8x8cj{ujxxc}cn4jguk}{4m}8k}c4{4u}9F8j99}uc}8g9{a8jam99c}88}j{	}cFu}}4amcxc}9jdxucxg}junm8dkxhuu8dk{9h88}jF8m{x4am8hxamu9cgc4x9nuj4cghlckukl4l}}}9{muc4kFummmcxmmll489d{aguhjx}hduhuhjjjc{4Fg}}jlgc98}xnkah8nx9cdumcuxg8}n8u9hccx9mau}4ju}8n}hx9lucnhx}n}h{cxckdln4kxku}d}u}lu4dxa4xg}}}88448k9ka4x}4xFkc}nj8}4xdx9k4un9gjuh9ju49n}9}98849cd9j8cu}du8h898{88mxj}k8m}k9c8n88}9uj}njxud9mxudan8knu4cm84ac}}88munnnx8c}djjd{8mcxkulmgh4x99k4muxd8c}k984umnun99h4}kkxk{}}k{hFa}nu8khxxljjaxjj8xn}nd9xdg}j{9dh{{n8mkju9kk}jj{9x{u4m}9k9}d}l}m4889k9{ndm4c}mkc9k{}acng9c{}k}FnFccn44hj8}89}uujc{94d4u}udF8mmhn4mdnl}hcxux9}894knFkk8mujdgaxkk4gd}4u4ux{xkxu8d{khm{}}8xnxg4}94u98hx94u}xlku9}9u}99cmm4}u}99Fm88du}dggunnl8x}h}9cugckg9ck}m49}cjlkk{c9kkn}nuujh}mF4n{{88d	d4}x}xcju9d8a8u8}xk8xudcmjgk}}48x9hhh88l9m8{m8gmd}ug}u}c99}ud4nhc88u4m}nga{kk4h{hxx8nh99xhunhcnh4u}c8d}x}}8ux'
qq=open('randlist.txt','r')
ww=qq.read()                            #读取文件

a=set(ww)                               #筛选有哪些字符
qwer={}                     

for s in a:                             #统计字符出现了多少次，再按照对应关系添加入字典中
    w=ww.count(s)
    qwer.update({s:w})


asdf=sorted(qwer.items(),key=lambda aaaa:aaaa[1])   #排序输出
for ass in asdf:
    #print(ass)
    print(ass[0],end='')






