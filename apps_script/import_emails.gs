/**
 * OPTIONAL: load the practice emails into a real (practice) Gmail account.
 * Not tested by the author, so try it on a throwaway account first.
 *
 * Setup:
 *  1. Sign in to the PRACTICE Gmail account, never your personal one.
 *  2. Upload data/emails.json to that account's Google Drive.
 *  3. Go to script.google.com > New project, paste this file.
 *  4. Left sidebar > Services (+) > add "Gmail API".
 *  5. Run importEmails() and approve the permissions.
 *
 * Only emails in folder "Inbox" are inserted. Messages arrive from the
 * practice account itself, so Gmail may show your practice address in the
 * "to" field. The original sender is kept in the From header.
 */
function importEmails() {
  var files = DriveApp.getFilesByName('emails.json');
  if (!files.hasNext()) throw new Error('Upload emails.json to Drive first.');
  var emails = JSON.parse(files.next().getBlob().getDataAsString());
  var me = Session.getActiveUser().getEmail();
  var count = 0;

  emails.forEach(function (e) {
    if (e.folder !== 'Inbox') return;
    var date = Utilities.formatDate(new Date(e.timestamp), 'GMT', 'EEE, dd MMM yyyy HH:mm:ss') + ' +0000';
    var raw = [
      'From: ' + e.sender,
      'To: ' + me,
      'Subject: ' + e.subject,
      'Date: ' + date,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset="UTF-8"',
      '',
      e.body
    ].join('\r\n');

    var labels = e.unread ? ['INBOX', 'UNREAD'] : ['INBOX'];
    Gmail.Users.Messages.insert(
      { raw: Utilities.base64EncodeWebSafe(raw), labelIds: labels },
      'me',
      null,
      { internalDateSource: 'dateHeader' }
    );
    count++;
  });
  Logger.log('Inserted ' + count + ' messages.');
}
