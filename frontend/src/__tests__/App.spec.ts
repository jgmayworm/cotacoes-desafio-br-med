import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import App from '../App.vue'

describe('App', () => {
  it('renderiza moeda e valor corretamente', () => {
    const wrapper = mount(App)
    expect(wrapper.text()).toContain('Cotações do Dólar')
  })
})
