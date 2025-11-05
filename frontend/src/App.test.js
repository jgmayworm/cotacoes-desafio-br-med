import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import App from './App.vue';
describe('App.vue', () => {
    it('renderiza título corretamente', () => {
        const wrapper = mount(App);
        expect(wrapper.text()).toContain('Cotações USD');
    });
});
