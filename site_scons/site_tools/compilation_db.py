
import SCons.Tool
import SCons.Defaults
import SCons.Util
import json

def db_entry(target, source, env):
    entries = []
    for s in source:
        source_suffix = s.suffix
        comstr = "$CCCOM" if (source_suffix in SCons.Tool.CSuffixes)  else "$CXXCOM"
        command = env.subst(comstr, target = s.target_from_source(env["OBJPREFIX"], env["OBJSUFFIX"] ), source = s.abspath)                                
        entry = { "directory" :  s.path_elements[-2].abspath,
                  "command" : command,
                  "file" :  s.abspath }
        entries.append(entry)
    db = open(target[0].path, "w")
    db.write(json.dumps(entries, indent = 4))
    db.close()
    return 0

def db_entry_str(target, source, env):
    return "Building %s " % target[0]

def exists(env):
    return True

def generate(env, **kwargs):
    try:
        dbbuilder = env["BUILDERS"]["CompilationDB"]
    except KeyError:
        import SCons.Defaults
        dbbuilder = SCons.Builder.Builder(action = SCons.Action.Action(db_entry, strfunction=db_entry_str),
                                          emitter = '$PROGEMITTER',
                                          suffix = '.json',
                                           src_builder = ['CFile', 'CXXFile'],
                                           source_scanner = SCons.Tool.SourceFileScanner)                                          
                                          
        env["BUILDERS"]["CompilationDB"] = dbbuilder
        


