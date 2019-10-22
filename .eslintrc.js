module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
    es6: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  plugins: [
    'vue',
  ],
  extends: [
    'prestashop',
    'plugin:vue/strongly-recommended',
  ],
  rules: {
    'vue/script-indent': [
      'error',
      2,
      {
        baseIndent: 1,
      },
    ],
  },
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        indent: 'off',
      },
    },
  ],
};
