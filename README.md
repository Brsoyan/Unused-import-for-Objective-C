# Unused-import-for-Objective-C
Remove Double imports from your project

Set your file path
project_path = "/Users/hb/Desktop/picsart-ios"

You can set file prefix which you need to find.
```
prefix = "HB"
```

If you need to remove unused categories imports chanage this BOOL value to True
```
remove_categories = False
```
# If in your project you have classes which #imports you doesn't need to remove.
# Or classes for static object
# Like this static NSString *CELL_IDENTIFIER = @"mainCell"; ....
# And does not need to delete import add the classes names in constant_classes list.

```
constant_classes = ["HBConstantString", "HBApiCallUrls"]
```
