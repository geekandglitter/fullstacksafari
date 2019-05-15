############################
# This function extracts a slug from a URL
#############################
def lmextractslug(theurl):
    newslug=theurl.rsplit('/',1)
    newslug=newslug[1]
    newslug=newslug[:-5]
    return(newslug)

def lmextractcontent(thecontent):
    printfriendly1="""<script>var pfHeaderImgUrl = '';var pfHeaderTagline = '';var pfdisableClickToDel = 0;var pfHideImages = 0;var pfImageDisplayStyle = 'right';var pfDisablePDF = 0;var pfDisableEmail = 0;var pfDisablePrint = 0;var pfCustomCSS = '';var pfBtVersion='2';(function(){var js,pf;pf=document.createElement('script');pf.type='text/javascript';pf.src='//cdn.printfriendly.com/printfriendly.js';document.getElementsByTagName('head')[0].appendChild(pf)})();</script><a class="printfriendly" href="https://www.printfriendly.com/" onclick="window.print();return false;" style="color: #6d9f00; text-decoration: none;" title="Printer Friendly and PDF"><img alt="Print Friendly and PDF" src="https://2.bp.blogspot.com/-_pA-Rf25q-g/Wz4GCdLo6XI/AAAAAAAAVKQ/PsFbM1HrvXofTuC0WbLFJ6Q4be1h2Y1HwCLcBGAs/s1600/printfriendly-button-md%2Bfinished%2Bwith%2Btan.jpg" style="-webkit-box-shadow: none; border: none; box-shadow: none;" /></a>"""
    printfriendly2="""<script>var pfHeaderImgUrl = '';var pfHeaderTagline = '';var pfdisableClickToDel = 0;var pfHideImages = 0;var pfImageDisplayStyle = 'right';var pfDisablePDF = 0;var pfDisableEmail = 0;var pfDisablePrint = 0;var pfCustomCSS = '';var pfBtVersion='2';(function(){var js,pf;pf=document.createElement('script');pf.type='text/javascript';pf.src='//cdn.printfriendly.com/printfriendly.js';document.getElementsByTagName('head')[0].appendChild(pf)})();</script><span style="font-size: small;"><span style="font-family: &quot;times&quot; , &quot;times new roman&quot; , serif;"><a class="printfriendly" href="https://www.printfriendly.com/" onclick="window.print();return false;" style="color: #6d9f00; text-decoration: none;" title="Printer Friendly and PDF"><img alt="Print Friendly and PDF" src="https://2.bp.blogspot.com/-_pA-Rf25q-g/Wz4GCdLo6XI/AAAAAAAAVKQ/PsFbM1HrvXofTuC0WbLFJ6Q4be1h2Y1HwCLcBGAs/s1600/printfriendly-button-md%2Bfinished%2Bwith%2Btan.jpg" style="-webkit-box-shadow: none; border: none; box-shadow: none;" /></a></span></span>"""
    printfriendly3="""<a class="printfriendly" href="https://www.printfriendly.com/" onclick="window.print();return false;" style="color: #6d9f00; text-decoration: none;" title="Printer Friendly and PDF"><img alt="Print Friendly and PDF" src="https://2.bp.blogspot.com/-_pA-Rf25q-g/Wz4GCdLo6XI/AAAAAAAAVKQ/PsFbM1HrvXofTuC0WbLFJ6Q4be1h2Y1HwCLcBGAs/s1600/printfriendly-button-md%2Bfinished%2Bwith%2Btan.jpg" style="-webkit-box-shadow: none; border: none; box-shadow: none;" /></a> <br />"""
    printfriendly4="""<a class="printfriendly" href="https://www.printfriendly.com/" onclick="window.print();return false;" style="color: #6d9f00; text-decoration: none;" title="Printer Friendly and PDF"><img alt="Print Friendly and PDF" src="https://2.bp.blogspot.com/-_pA-Rf25q-g/Wz4GCdLo6XI/AAAAAAAAVKQ/PsFbM1HrvXofTuC0WbLFJ6Q4be1h2Y1HwCLcBGAs/s1600/printfriendly-button-md%2Bfinished%2Bwith%2Btan.jpg" style="-webkit-box-shadow: none; border: none; box-shadow: none;" /></a><br />"""
    pythonista1="""<h2>
I belong to a private, fee-based group of Pythonistas. </h2>
If you would like to know more about <a href="https://www.pythonistacafe.com/">PythonistaCafe</a>, where we share thoughts, ideas, fixes, and a sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by email.

Oh, and if you take an interest in good marketing writing, read his stuff for that reason too.&nbsp; """
    pythonista2="""<h2>
I belong to a private, fee-based group of Pythonistas. </h2>
If you would like to know more about <a href="https://www.pythonistacafe.com/">PythonistaCafe</a>, where we share thoughts, ideas, fixes, and a sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by email.  Oh, and if you take an interest in good marketing writing, read his stuff for that reason too."""
    pythonista3="""<h2>
I belong to a private, fee-based group of Pythonistas. </h2>
&nbsp;If you would like to know more about <a href="https://www.pythonistacafe.com/">PythonistaCafe</a>, where we share thoughts, ideas, fixes, and a<br />
&nbsp;sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by<br />
&nbsp;email.&nbsp;  Oh, and if you take an interest in good marketing writing, read his stuff for that reason too.&nbsp;  """
    pythonista4="""<h2>I belong to a private, fee-based group of Pythonistas. </h2>If you would like to know more about <a href="https://www.pythonistacafe.com/">PythonistaCafe</a>, where we share thoughts, ideas, fixes, and a sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by email.  Oh, and if you take an interest in good marketing writing, read his stuff for that reason too."""
    pythonista5="""<h2>I belong to a private, fee-based group of Pythonistas&nbsp;</h2>If you would like to know more about a group of Pythonistas who share thoughts, ideas, fixes, and a sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by email.<br /><br />Oh, and if you take an interest in good marketing writing, read his stuff for that reason too."""
    pythonista5="""If you would like to know more about a group of Pythonistas who share thoughts, ideas, fixes, and a sense of courteous community, look to Dan Bader, who started it all. He also offers free tips by email. Oh, and if you take an interest in good marketing writing, read his stuff for that reason too."""
    pythonista6="""<h2>I belong to a private, fee-based group of Pythonistas&nbsp;</h2>If you would like to know more about a group of Pythonistas who share thoughts, ideas, fixes, and a sense of courteous community, look to <a href="https://dbader.org/" target="_blank">Dan Bader</a>, who started it all. He also offers free tips by email.<br /><br />Oh, and if you take an interest in good marketing writing, read his stuff for that reason too."""
    newcontent1=thecontent.replace(printfriendly1, '')
    newcontent2=newcontent1.replace(printfriendly2, '')
    newcontent3=newcontent2.replace(printfriendly3, '')
    newcontent4=newcontent3.replace(printfriendly4, '')
    newcontent5=newcontent4.replace(pythonista1, '')
    newcontent6 = newcontent5.replace(pythonista2, '')
    newcontent7=newcontent6.replace(pythonista3, '')
    newcontent8 = newcontent7.replace(pythonista4, '')
    newcontent9 = newcontent8.replace(pythonista5, '')
    newcontent10 = newcontent9.replace(pythonista6, '')
    return(newcontent10)




