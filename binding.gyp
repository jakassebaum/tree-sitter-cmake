{
  "targets": [
    {
      "target_name": "tree_sitter_cmake_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "src",
      ],
      "defines": [
        "NAPI_DISABLE_CPP_EXCEPTIONS"
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
        "src/scanner.c",
        # NOTE: if your language has an external scanner, add it here.
      ],
      "cflags_c": [
        "-std=c11",
      ],
    }
  ]
}
