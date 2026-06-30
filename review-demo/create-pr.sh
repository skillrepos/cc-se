// review-demo/user-store.js
//
// Intentional review demo for Lab 12 (claude ultrareview).
// This file ships with several DELIBERATE, real issues so the deep CI review
// has something concrete to find. It is not used by the app — it exists only
// so students can run `claude ultrareview` against a live PR.

const db = require("./fake-db");

// Issue 1 (security): hardcoded secret committed to source control.
const API_KEY = "sk-live-9f3c2a77b1e4please-rotate-me";

// Issue 2 (security): token built from Math.random — not cryptographically
// secure, and predictable.
function newSessionToken() {
  return "tok_" + Math.random().toString(36).slice(2);
}

// Issue 3 (security): SQL injection — userId is concatenated straight into the
// query instead of being passed as a parameter.
async function findUser(userId) {
  const sql = "SELECT * FROM users WHERE id = '" + userId + "'";
  return db.query(sql);
}

// Issue 4 (correctness/security): loose equality lets "0", 0, "", and false all
// pass as the same admin check; should be strict (===) against a real role.
function isAdmin(user) {
  return user.role == 1;
}

// Issue 5 (correctness): the promise is never awaited and errors are swallowed,
// so a failed lookup silently returns undefined and logs the password.
function login(userId, password) {
  let result;
  findUser(userId).then((u) => {
    console.log("login attempt", userId, password); // logs the password
    result = u;
  });
  return result;
}

module.exports = { API_KEY, newSessionToken, findUser, isAdmin, login };
