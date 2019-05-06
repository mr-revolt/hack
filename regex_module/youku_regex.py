import re

html = '''
<div class="sk-mod">
	<div class="mod-left">
	<a class="sk-pack" data-spm="dposter" target="_blank" href="//v.youku.com/v_show/id_XNDA3NjM3OTc2OA==.html">
		<div class="pack-cover">
		<img class="" src="//r1.ykimg.com/054101015C7230E1ADCA619A3DB794B0">		
		</div>
		<span class="pack-rb pack-time">06:19</span>
		<span class="pack-lb"><i class="iku-download" title="使用客户端下载此片" data-down="video" data-iku-down-id="XNDA3NjM3OTc2OA==" data-id="1019094942" _log_ct="&quot;4&quot;" _log_type="&quot;3&quot;"></i></span>
			
	</a>		
	</div>
	<div class="mod-main">
		<div class="mod-header">
<h2 class="spc-lv-1">
	<a target="_blank" data-spm="dtitle" title="《HELLO》Adele阿黛尔史诗级巨献 唱碎亿万听众的心" href="//v.youku.com/v_show/id_XNDA3NjM3OTc2OA==.html">《<em class="hl">HELLO</em>》Adele阿黛尔史诗级巨献 唱碎亿万听众的心</a>
</h2>
		</div>
		<div class="mod-info">
			<p>
				<span class="spc-lv-4"><label>上传时间:</label>2019-2-24 </span>
				<span class="spc-lv-4"><label>上传者:</label><a data-spm="dname" target="_blank" href="//i.youku.com/u/UNjQ5NDU4Mzc2OA==">千秋画音乐</a></span>
			</p>
		</div>
		<div class="mod-play">

		</div>
	</div>
</div>
'''
youkufile_regex = re.compile(r'^title="(.*?)"\shref="(.*?)".*?</h2>$">')
res = re.findall(youkufile_regex,html,re.S)
print(res)
