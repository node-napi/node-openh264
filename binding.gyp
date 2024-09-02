{
  'targets': [
    {
      'target_name': 'node-openh264',
      'sources': [ 'src/node-openh264.cc' ],
      'libraries': [
         "<(module_root_dir)/includes/libopenh264.a",
      ],
      'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")",
                       "<(module_root_dir)/includes"],
      'dependencies': [
          "<!(node -p \"require('node-addon-api').gyp\")",
          "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except"
       ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ]
}