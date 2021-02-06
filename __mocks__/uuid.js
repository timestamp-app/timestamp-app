const uuid = jest.createMockFromModule('uuid')

function v4() {
  return '1f83f6a2-3841-45da-8129-98de28ce7b74'
}

uuid.v4 = v4

module.exports = uuid
