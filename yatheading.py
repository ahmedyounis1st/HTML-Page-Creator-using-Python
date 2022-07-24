from simpletag import STag

def headmeta(doc, content=''):
    doc += STag('meta', charset="UTF-8")
    doc += STag('meta', name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
    doc += STag('meta', name="description", content="%s" % (content))
    #with doc.tag('script', src="{{ url_for('static', path='js/jquery-3.4.1.min.js') }}", rel="stylesheet"):
    with doc.tag('script', src="static/js/jquery-3.4.1.min.js", rel="stylesheet"):
    #with doc.tag('script', src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js", type="text/javascript"):
        pass

def styling(doc, bs='border-style: solid;'):
    doc += ('table, th, td { border-collapse: collapse; %s }' % (bs))
    doc += ('th, td { padding: 5px; overflow-wrap: break-word; }')
    doc += ('table.border td { border:1px solid black; }')
    doc += ('button:hover    { opacity: 0.8; }')
    doc += ('button:active   { background-color: #006400; box-shadow: 0 5px #666; transform: translateY(4px); }')
    doc += ('.style-lf                 { text-align: left; }')
    doc += ('.style-lf-fz150           { text-align: left;   font-size: 150%; }')
    doc += ('.style-lf-fz120-lblue     { text-align: left;   font-size: 120%; background-color: #00AAE4; }')
    doc += ('.style-lf-bo-fz120        { text-align: left;   font-weight: bold; font-size: 120%; }')
    doc += ('.style-lf-bo              { text-align: left;   font-weight: bold; }')
    doc += ('.style-lf-bo-bglblue      { text-align: left;   font-weight: bold; background-color: #00AAE4; color: #FFFFFF; }')
    doc += ('.style-lf-bo-bgblack      { text-align: left;   font-weight: bold; background-color: #000000; color: #FFFFFF; }')
    doc += ('.style-lf-bo-bgdkred      { text-align: left;   font-weight: bold; background-color: #900C3F; color: #FFFFFF; }')
    doc += ('.style-lf-bo-bgpurple     { text-align: left;   font-weight: bold; background-color: #8A2BE2; color: #FFFFFF; }')
    doc += ('.style-ct-bo-bgdkgreen    { text-align: center; font-weight: bold; background-color: #006400; color: #FFFFFF; }')
    doc += ('.style-ct-bo-bglmgreen    { text-align: center; font-weight: bold; background-color: #32CD32; }')
    doc += ('.style-button-fz125-time  { text-align: center; font-size: 125%; font-family:"Times New Roman"; padding-left: 10px; padding-right: 10px;}')
    doc += ('.style-misc               { text-align: left; max-width: 30vw; vertical-align: text-top; }')
    doc += ('.style-ct                 { text-align: center; }')
    doc += ('.style-base-fz            { font-size: 1vw; }')
    doc += ('.scale-base    { background-color: #FDFFF5; padding: 20px; font-size: 1vw; }')
    doc += ('@media only screen and (max-width: 1000px) { .scale-base { font-size: 3vw; } .style-base-fz { font-size: 3vw; } }')
    doc += ('.responsive    { width: auto; max-width: 100%; height: auto; }')
    doc += ('.radio-valign [type="radio"] { vertical-align: middle; }')
    doc += ('.vertical { text-align:center; transform: rotate(270deg); }')
    doc += ('.wrapcell { width: 200px; word-wrap: break-word; }')
