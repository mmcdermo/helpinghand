class R_Expr:
    def __init__(self,r_type,r_restrictions,r_set):
        self.expression_type = r_type
        self.restrictions = r_restrictions
        self.target_set = r_set
    def show(self,key,title,desc):
        #always need this just to be able to retrieve things from database
        result = self.expression_type.showImports(self.target_set)
        result += self.restrictions.show()
        result += self.expression_type.show(key,self.target_set,title,desc)

        return result

class R_Type:
    def __init__(self,t):
        self.type_symbol = t

    def showImports(self, ts):
        if self.type_symbol == 'S':
            result = "from %s.views import get%s\n" % (ts.app,ts.model)
            result += "from %s.models import %s\n" % (ts.app,ts.model)
            result += "qs = %s.objects.all()\n" % ts.model
            return result
            
        if self.type_symbol == 'F':
            return "from %s.forms import %sForm\n" % (ts.app,ts.model)

    def show(self,key,ts,title,desc):
        result = "from django.template import RequestContext\n"
        result += "d['%s'] = " % key
        if self.type_symbol == 'S':
            result += "get%s(qs)\n" % ts.model
        if self.type_symbol == 'F':
            result += "render_to_string('form.html', {'title':'%s', 'description': '%s', 'action':'/api/%s/%s/create/','formFields':%sForm().as_p()},context_instance=RequestContext(request))\n" % (title,desc,ts.app,ts.model,ts.model)

        return result

class R_Restrictions:
    def __init__(self,restrictions):
        self.restrictions = restrictions

    def showEquality(self, r):
        """TODO: Needs to eventually deal with types"""
        return "qs = qs.filter(%s=%s)\n" % (r[0],r[2].replace('%','u_'))

    def showFilter(self, r):
        """Given a key and a value do something with it"""
        #the key tells us what to do
        if r[0] == "limit":
            return "qs = qs[:%s]\n" % r[2]
        elif r[0] == "offset":
            return "qs = qs[%s:]\n" % r[2]
        elif r[0] == "sortby":
            return "qs = qs.order_by('%s')\n" % r[2]
        return ""

    def show(self):
        #restrictions are a tuple (field,op,value) different ops imply different logic
        result = ""
        for restriction in self.restrictions:
            if restriction[1] == '=':
                result += self.showEquality(restriction)
            elif restriction[1] == ':':
                result += self.showFilter(restriction)

        return result

class R_Set:
    def __init__(self,app,model):
        self.app = app
        self.model = model

    def showUserCase(self):
        return ""

    def show(self):
        return "(%s->%s)" %(self.app, self.model)

    
d = {"pages":{"page":{"pageData":{"expr":R_Expr(R_Type("S"),R_Restrictions([("title","=","%1")]),R_Set("page","Page")),"type":"expr"},"template":"%pageData%","url":"page/(.*)/","title":"Page"},"menu":{"menuItems":{"expr":R_Expr(R_Type("S"),R_Restrictions([("menu","=","%1")]),R_Set("page","Item")),"type":"expr"},"template":"%menuItems%","url":"menu/(.*)/","title":"Menu"},"home":{"template":"","url":"","title":"Homepage"}},"menu":{},"database":{"engine":"django.db.backends.sqlite3","name":"db.db"},"apps":{"page":{"models":{"Page":{"display":"<h1>%title%</h1><div>%content%</div>","listing":"","admin":"%title","fields":{"content":{"type":"TextField"},"title":{"length":32,"type":"CharField"}}},"Item":{"display":"<a id='%targetType%.%target%' href='#'>%title%</a>","listing":"<a id='%targetType%.%target%' href='#'>%title%</a>","admin":"%title","fields":{"target":{"optional":"True","length":32,"type":"CharField"},"targetType":{"length":32,"type":"CharField"},"menu":{"length":32,"type":"CharField"},"title":{"length":32,"type":"CharField"}}}}}},"website":{"admins":{"c":{"email":"crowe.jb@gmail.com","name":"Jeremy Crowe"},"b":{"email":"morganmcdermott@gmail.com","name":"Morgan McDermott"},"a":{"email":"john.w.carlyle@gmail.com","name":"John Carlyle"}},"author":"John Carlyle, Jeremy Crowe, and Morgan McDermott","prettyName":"Helping Hand","name":"HelpingHandServer"}}

