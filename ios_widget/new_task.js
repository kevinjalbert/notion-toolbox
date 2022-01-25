let alert = new Alert()
alert.title = "New Task"
alert.addTextField();
alert.addAction("Add Task");
alert.addCancelAction("Cancel")
await alert.presentAlert();
let task = alert.textFieldValue(0)
if (task){

  let req = new Request("https://api.notion.com/v1/pages");
  req.method = "post";
  req.headers = {
  'Authorization': 'Bearer '+ args.queryParameters.token,
  'Notion-Version': '2021-08-16',
  "Content-Type": "application/json"
  };
    
  req.body = JSON.stringify({
    "parent": {
      "database_id":  args.queryParameters.parent_id
    },
    "properties": {
      "State": {
        "type": "select",
        "select": {
          "name": "Open"
        }
      },
      "Name": {
        "title": [
          {
            "text": {
              "content": task
            }
          }
        ]
      }
    }
  });
  
  const res = await req.loadJSON()

   let refresh = new CallbackURL("scriptable:///run/")
   refresh.addParameter("scriptName", "to_do")
   refresh.addParameter("limit" , args.queryParameters.limit.toString())
   refresh.addParameter("parent_id", args.queryParameters.parent_id.toString())
   refresh.open()
  
}
else {
  App.close()
}
function get_week(date){
  var oneJan = new Date(date.getFullYear(),0,1);
  var numberOfDays = Math.floor((date - oneJan) / (24 * 60 * 60 * 1000));
  var resultq = Math.ceil(( date.getDay() + 1 + numberOfDays) / 7);
return resultq;
}
