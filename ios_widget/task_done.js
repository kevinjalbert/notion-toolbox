let req = new Request("https://api.notion.com/v1/pages/" + args.queryParameters.id);
req.method = "PATCH";
req.headers = {
	'Authorization': 'Bearer ' + args.queryParameters.token,
  'Notion-Version': '2021-08-16',
	"Content-Type": "application/json"
};
  
req.body = JSON.stringify({
   "properties":{
      "State":{
         "select":{
            "name":"Done"
         }
      }
   }
});

const res = await req.loadJSON()


let refresh = new CallbackURL("scriptable:///run/")
refresh.addParameter("scriptName", "to_do")
refresh.addParameter("limit" , args.queryParameters.limit.toString())
refresh.addParameter("parent_id", args.queryParameters.parent_id.toString())
refresh.open()
