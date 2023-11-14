from senzing import g2configmgr, g2diagnostic, g2exception

g2_diagnostic = g2diagnostic.G2Diagnostic()

engine_vars = {
    "MODULE_NAME": "Testing",
    "VERBOSE_LOGGING": 0,
    "INI_PARAMS": '{"PIPELINE": {"CONFIGPATH": "/etc/opt/senzing", "RESOURCEPATH": "/opt/senzing/g2/resources", "SUPPORTPATH": "/opt/senzing/data"}, "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"}}',
}

def test_init_and_destroy(g2_diagnostic, engine_vars):
    print('In 1')
    g2_diagnostic.init(engine_vars["MODULE_NAME"], engine_vars["INI_PARAMS"], 0)
    g2_diagnostic.destroy()
    print('Out 1')


def test_init_and_destroy_2(g2_diagnostic, engine_vars):
    print("In 2")
    g2_diagnostic.init(engine_vars["MODULE_NAME"], engine_vars["INI_PARAMS"], 0)
    g2_diagnostic.destroy()
    print('Out 2')

test_init_and_destroy(g2_diagnostic, engine_vars)
test_init_and_destroy_2(g2_diagnostic, engine_vars)
